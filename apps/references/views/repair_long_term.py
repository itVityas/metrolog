from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import VerificationLogForm
from django.db.models.functions import Extract
from django.db.models import OuterRef, Subquery


class RepairLongTermView(LoginRequiredMixin, TemplateView):
    """
        СИ в долгосрочном ремонте
    """
    template_name = 'references/repair_long_term.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_repair_info_query = pmodels.RepairInfo.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-entry_date')

        latest_device_location_query = pmodels.DeviceLocation.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-entry_date')

        latest_device_status_query = pmodels.DeviceStatusDate.objects.filter(
            moc_list=OuterRef('pk')
            ).order_by('-id')

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group',
            'change_type').annotate(
                entry_date=Subquery(
                    latest_repair_info_query.values(
                        'entry_date')[:1]),
                repair_type=Subquery(
                    latest_repair_info_query.values(
                        'repair_type')[:1]),
                repair_date=Subquery(
                    latest_repair_info_query.values(
                        'repair_date')[:1]),
                instrument_failure=Subquery(
                    latest_repair_info_query.values(
                        'instrument_failure__name')[:1]),
                last_device_location=Subquery(
                    latest_device_location_query.values(
                        'department__name')[:1]),
                last_device_status=Subquery(
                    latest_device_status_query.values(
                        'device_status__name')[:1]),
                ).filter(
                    last_device_status='Долгоср-й рем.',
                    ).order_by(
                        'change_type__name')

        result_list = []
        prev_change_type = None
        list_to_add = []
        for q in queryset:
            if prev_change_type is None:
                prev_change_type = q.change_type
            if prev_change_type != q.change_type:
                result_list.append({'change_type': prev_change_type.name,
                                    'values': list_to_add})
                list_to_add = []
                prev_change_type = q.change_type
            list_to_add.append(q)

        for elem in result_list:
            if elem['location'] == '"Исп.центр центр"':
                elem['location'] = 'Исп.центр'
            if elem['location'] == 'Тех.центр центр центр':
                elem['location'] = 'Тех.центр'

        context['result_list'] = result_list
        return self.render_to_response(context)
