from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
import datetime
from ..forms import MemorandumForm
from django.shortcuts import render
from django.db.models.functions import Extract
from django.db.models import OuterRef, Subquery


class PrescriptionView(LoginRequiredMixin, TemplateView):
    """
        Предписание (кроме встроенных)
    """
    template_name = 'references/prescription.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_device_location_query = pmodels.DeviceLocation.objects.filter(
            moc_list=OuterRef('pk')
            ).order_by('-id')

        latest_verification_info_query = pmodels.VerificationInfo.objects.filter(
            moc_list=OuterRef('pk')
            ).exclude(
                verification_date=None,
                ).order_by('-verification_date')

        latest_device_status_query = pmodels.DeviceStatusDate.objects.filter(
            moc_list=OuterRef('pk')
            ).order_by('-id')

        form = MemorandumForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            workshop = form.cleaned_data['workshop']
            brigade = form.cleaned_data['brigade']

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info').annotate(
                    last_location_name=Subquery(
                        latest_device_location_query.values(
                            'department__name')[:1]),
                    last_location_workshop=Subquery(
                        latest_device_location_query.values(
                            'department__workshop')[:1]),
                    last_location_brigade=Subquery(
                        latest_device_location_query.values(
                            'department__brigade')[:1]),
                    last_verification_date=Subquery(
                        latest_verification_info_query.values(
                            'verification_date')[:1]),
                    last_device_status=Subquery(
                        latest_device_status_query.values(
                            'device_status__name')[:1]),
                    ).filter(
                        verification_period__lte=(
                            Extract(start_date, 'year') -
                            Extract('last_verification_date',
                                    'year')) * 12 +
                        (Extract(start_date, 'month') -
                            Extract('last_verification_date',
                                    'month')),
                        last_device_status='В эксплуатации',
                        device_location__department__workshop=workshop,
                        device_location__department__brigade=brigade).exclude(
                            sign_o_m=pmodels.MocList.SignOM.BUILTIN
                            ).exclude(
                                last_verification_date__month=Extract(start_date, 'month'),).order_by(
                                    'verification_type', '-change_type')

        location_name = queryset.first().last_location_name
        if location_name == '"Исп.центр центр"':
            location_name = '"Исп.центр'
        context['location_name'] = location_name
        context['start_date'] = start_date
        context['queryset'] = queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = MemorandumForm()
        return render(request,
                      'references/modals/prescription_modal.html',
                      {'form': form})
