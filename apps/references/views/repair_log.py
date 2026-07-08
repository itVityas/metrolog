from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import VerificationLogForm
from django.db.models.functions import Extract
from django.db.models import OuterRef, Subquery


class RepairLogView(LoginRequiredMixin, TemplateView):
    """
        Журнал ремонта
    """
    template_name = 'references/repair_log.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = VerificationLogForm(request.POST)
        if form.is_valid():
            change_type = form.cleaned_data['change_type']
            start_date = form.cleaned_data['start_date']

        latest_repair_info_query = pmodels.RepairInfo.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-entry_date')

        latest_device_location_query = pmodels.DeviceLocation.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-entry_date')

        queryset = pmodels.MocList.objects.select_related(
            'moc_type').annotate(
                entry_date=Subquery(
                    latest_repair_info_query.values(
                        'entry_date')[:1]),
                instrument_failure=Subquery(
                    latest_repair_info_query.values(
                        'instrument_failure__name')[:1]),
                entry_repair_date=Subquery(
                    latest_repair_info_query.values(
                        'entry_repair_date')[:1]),
                repair_department=Subquery(
                    latest_repair_info_query.values(
                        'repair_department__name')[:1]),
                repair_date=Subquery(
                    latest_repair_info_query.values(
                        'repair_date')[:1]),
                last_device_location=Subquery(
                    latest_device_location_query.values(
                        'department__name')[:1])
                ).filter(
                    entry_date__lte=start_date,
                    change_type=change_type,
                    repair_date=None).exclude(
                        entry_date=None).order_by(
                            'last_device_location')

        result_list = []
        prev_location = None
        total_sum = 0
        list_to_add = []
        for q in queryset:
            if prev_location is None:
                prev_location = q.last_device_location
            if prev_location != q.last_device_location:
                result_list.append({'location': prev_location,
                                    'total_count': total_sum,
                                    'values': list_to_add})
                total_sum = 0
                list_to_add = []
                prev_location = q.last_device_location
            if q.moc_type.standart_repair is not None:
                total_sum += q.moc_type.standart_repair
            list_to_add.append(q)

        context['start_date'] = start_date
        context['result_list'] = result_list
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = VerificationLogForm()
        return render(request,
                      'references/modals/repair_log_modal.html',
                      {'form': form})
