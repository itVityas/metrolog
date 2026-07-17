from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import OperatingTimeForm
from django.db.models.functions import Extract
from django.db.models import OuterRef, Subquery


class EconomVerifCostsView(LoginRequiredMixin, TemplateView):
    """
        Затраты подразделений на госповерку за месяц
    """
    template_name = 'references/econom_verif_costs.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = OperatingTimeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']

        latest_verification_info_query = pmodels.VerificationInfo.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-verification_date')

        latest_device_location_query = pmodels.DeviceLocation.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-entry_date')

        actual_device_status_query = pmodels.DeviceStatusDate.objects.filter(
            moc_list=OuterRef('pk'),
            status_date__lte=start_date
        ).order_by('-status_date')

        queryset = pmodels.MocList.objects.select_related(
            'moc_type').annotate(
                last_verification_date=Subquery(
                    latest_verification_info_query.values(
                        'verification_date')[:1]),
                last_device_location=Subquery(
                    latest_device_location_query.values(
                        'department__name')[:1]),
                actual_device_status=Subquery(
                    actual_device_status_query.values(
                        'device_status__name')[:1]),
                ).filter(
                    verification_type=pmodels.MocList.VerificationType.GOVERNMENTAL,
                    verification_period__lte=(
                        Extract(start_date, 'year') -
                        Extract('last_verification_date', 'year')) * 12 +
                    (Extract(start_date, 'month') -
                        Extract('last_verification_date', 'month'))
                    ).exclude(
                        actual_device_status='На хранении').order_by(
                            'last_device_location')

        result_list = []
        prev_location = None
        list_to_add = []
        for q in queryset:
            if prev_location is None:
                prev_location = q.last_device_location
            if q.last_device_location == 'Бюро1521' or q.last_device_location == 'Бюро 1523':
                continue
            if prev_location != q.last_device_location:
                result_list.append({'location': prev_location,
                                    'values': list_to_add})
                list_to_add = []
                prev_location = q.last_device_location
            list_to_add.append(q)

        context['start_date'] = start_date
        context['result_list'] = result_list
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = OperatingTimeForm()
        return render(request,
                      'references/modals/econom_verif_costs_modal.html',
                      {'form': form})
