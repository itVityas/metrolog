from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import MocPresenceForm
from django.db.models.functions import Extract
from django.db.models import OuterRef, Subquery


class MocPresenceView(LoginRequiredMixin, TemplateView):
    """
        Наличие СИ в подразделении (кроме встроенных)
    """
    template_name = 'references/moc_presence.html'

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

        form = MocPresenceForm(request.POST)
        if form.is_valid():
            change_type_list = form.cleaned_data['change_type']
            department = form.cleaned_data['department']

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info',
                'device_location',
                'device_status_date').annotate(
                    last_location=Subquery(
                        latest_device_location_query.values(
                            'department')[:1]),
                    last_device_status=Subquery(
                        latest_device_status_query.values(
                            'device_status__name')[:1]),
                    last_verification_date=Subquery(
                        latest_verification_info_query.values(
                            'verification_date')[:1]),
                    ).filter(
                        change_type__in=change_type_list,
                        last_location=department).exclude(
                            sign_o_m=pmodels.MocList.SignOM.BUILTIN
                            ).order_by('moc_type__type')

        if department.name == '"Исп.центр центр"':
            department.name = 'Исп.центр'
        if department.name == 'Тех.центр центр центр':
            department.name = 'Тех.центр'
        context['department'] = department.name
        context['queryset'] = queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = MocPresenceForm()
        return render(request,
                      'references/modals/moc_presence_modal.html',
                      {'form': form})
