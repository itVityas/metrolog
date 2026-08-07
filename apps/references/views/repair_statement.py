from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import OperatingTimeForm
from django.db.models.functions import Extract
from django.db.models import Count, Sum, Avg
from django.db.models import F
from datetime import date
import calendar
from django.db.models import OuterRef, Subquery


class RepairStatementView(LoginRequiredMixin, TemplateView):
    """
        Ведомость ремонтов за месяц
    """
    template_name = 'references/repair_statement.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = OperatingTimeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']

        start_year = start_date.year
        start_month = start_date.month
        _, last_day = calendar.monthrange(start_year, start_month)

        latest_device_location_query = pmodels.DeviceLocation.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-entry_date')

        latest_device_location_query = pmodels.DeviceLocation.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-entry_date')

        latest_device_status_query = pmodels.DeviceStatusDate.objects.filter(
            moc_list=OuterRef('pk')
            ).order_by('-id')

        start_of_year = date(start_year, 1, 1)
        end_date = date(start_year, start_month, last_day)

        queryset_month = pmodels.MocList.objects.prefetch_related(
            'repair_info',
            'device_location'
            ).annotate(
                last_device_location=Subquery(
                    latest_device_location_query.values(
                        'department__name')[:1]),
                last_device_status=Subquery(
                    latest_device_status_query.values(
                        'device_status__name')[:1]),
                ).exclude(
                    repair_info__repair_date=None
                    ).filter(
                        repair_info__repair_date__year=Extract(start_date, 'year'),
                        repair_info__repair_date__month=Extract(start_date, 'month')
                        ).values(
                            location_name=F('last_device_location'),
                            ).annotate(
                                repair_count=Count('moc_type'),
                                standart_sum=Sum('moc_type__standart_repair'),
                                avg_rank=Avg('moc_type__rank_repair')
                                ).order_by('location_name')

        queryset_year = pmodels.MocList.objects.prefetch_related(
            'repair_info',
            'device_location').annotate(
                last_device_location=Subquery(
                    latest_device_location_query.values(
                        'department__name')[:1]),
                last_device_status=Subquery(
                    latest_device_status_query.values(
                        'device_status__name')[:1]),
                ).filter(
                    repair_info__repair_date__range=(start_of_year, end_date)
                    ).values(
                        location_name=F('last_device_location'),
                        ).annotate(
                            repair_count=Count('moc_type'),
                            standart_sum=Sum('moc_type__standart_repair'),
                            avg_rank=Avg('moc_type__rank_repair')
                            ).order_by('location_name')

        sum_queryset = {
            'month_repair_count': 0,
            'month_standart_sum': 0,
            'year_repair_count': 0,
            'year_standart_sum': 0,
        }
        for qm in queryset_month:
            sum_queryset['month_repair_count'] += qm['repair_count']
            sum_queryset['month_standart_sum'] += qm['standart_sum']
        for qy in queryset_year:
            sum_queryset['year_repair_count'] += qy['repair_count']
            sum_queryset['year_standart_sum'] += qy['standart_sum']

        result_queryset = []
        temp_dict = {'location_name': '',
                     'month_repair_count': '',
                     'month_standart_sum': '',
                     'month_avg_rank': '',
                     'year_repair_count': '',
                     'year_standart_sum': '',
                     'year_avg_rank': ''}
        for qy in queryset_year:
            temp_dict['location_name'] = qy['location_name']
            temp_dict['year_repair_count'] = qy['repair_count']
            temp_dict['year_standart_sum'] = qy['standart_sum']
            temp_dict['year_avg_rank'] = qy['avg_rank']
            for qm in queryset_month:
                if qy['location_name'] == qm['location_name']:
                    temp_dict['month_repair_count'] = qm['repair_count']
                    temp_dict['month_standart_sum'] = qm['standart_sum']
                    temp_dict['month_avg_rank'] = qm['avg_rank']
            result_queryset.append(temp_dict)
            temp_dict = {'location_name': '',
                         'month_repair_count': '',
                         'month_standart_sum': '',
                         'month_avg_rank': '',
                         'year_repair_count': '',
                         'year_standart_sum': '',
                         'year_avg_rank': ''}

        for elem in result_queryset:
            if elem['location_name'] == '"Исп.центр центр"':
                elem['location_name'] = 'Исп.центр'
            if elem['location_name'] == 'Тех.центр центр центр':
                elem['location_name'] = 'Тех.центр'

        context['start_date'] = start_date
        context['queryset'] = result_queryset
        context['sum_queryset'] = sum_queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = OperatingTimeForm()
        return render(request,
                      'references/modals/repair_statement_modal.html',
                      {'form': form})
