from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import EconomVerifCostsPeriodForm
from django.db.models.functions import Extract
from django.db.models import Count, Sum, Avg
from django.db.models import F
from datetime import date
import calendar


class EconomVerifCostsPeriodView(LoginRequiredMixin, TemplateView):
    """
        Затраты структурных подразделений на поверку СИ
    """
    template_name = 'references/econom_verif_costs_period.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = EconomVerifCostsPeriodForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            period = form.cleaned_data['period']

        start_year = start_date.year
        start_month = start_date.month
        _, last_day = calendar.monthrange(start_year, start_month)

        start_of_year = date(start_year, 1, 1)
        end_date = date(start_year, start_month, last_day)

        match period:
            case 'month':
                queryset_gov = pmodels.VerificationInfo.objects.select_related(
                    'moc_list').prefetch_related('moc_list__device_location').filter(
                        verification_date__year=Extract(start_date, 'year'),
                        verification_date__month=Extract(start_date, 'month'),
                        moc_list__verification_type=pmodels.MocList.VerificationType.GOVERNMENTAL).values(
                            location_name=F('moc_list__device_location__department__name'),
                            ).annotate(
                                verification_count=Count('moc_list__moc_type'),
                                standart_sum=Sum('moc_list__moc_type__standart_verification'),
                                avg_rank=Avg('moc_list__moc_type__rank_verification')
                                ).order_by('location_name')
                queryset_dep = pmodels.VerificationInfo.objects.select_related(
                    'moc_list').prefetch_related('moc_list__device_location').filter(
                        verification_date__year=Extract(start_date, 'year'),
                        verification_date__month=Extract(start_date, 'month'),
                        moc_list__verification_type=pmodels.MocList.VerificationType.DEPARTMENTAL).values(
                            location_name=F('moc_list__device_location__department__name'),
                            ).annotate(
                                verification_count=Count('moc_list__moc_type'),
                                standart_sum=Sum('moc_list__moc_type__standart_verification'),
                                avg_rank=Avg('moc_list__moc_type__rank_verification')
                                ).order_by('location_name')
            case 'year':
                queryset_gov = pmodels.VerificationInfo.objects.select_related(
                    'moc_list').prefetch_related('moc_list__device_location').filter(
                        verification_date__year=Extract(start_date, 'year'),
                        moc_list__verification_type=pmodels.MocList.VerificationType.GOVERNMENTAL).values(
                            location_name=F('moc_list__device_location__department__name'),
                            ).annotate(
                                verification_count=Count('moc_list__moc_type'),
                                standart_sum=Sum('moc_list__moc_type__standart_verification'),
                                avg_rank=Avg('moc_list__moc_type__rank_verification')
                                ).order_by('location_name')
                queryset_dep = pmodels.VerificationInfo.objects.select_related(
                    'moc_list').prefetch_related('moc_list__device_location').filter(
                        verification_date__year=Extract(start_date, 'year'),
                        moc_list__verification_type=pmodels.MocList.VerificationType.DEPARTMENTAL).values(
                            location_name=F('moc_list__device_location__department__name'),
                            ).annotate(
                                verification_count=Count('moc_list__moc_type'),
                                standart_sum=Sum('moc_list__moc_type__standart_verification'),
                                avg_rank=Avg('moc_list__moc_type__rank_verification')
                                ).order_by('location_name')

        sum_queryset = {
            'gov_verification_count': 0,
            'gov_standart_sum': 0,
            'dep_verification_count': 0,
            'dep_standart_sum': 0,
        }
        for q_gov in queryset_gov:
            sum_queryset['gov_verification_count'] += q_gov['verification_count'] if q_gov['verification_count'] else 0
            sum_queryset['gov_standart_sum'] += q_gov['standart_sum'] if q_gov['standart_sum'] else 0
        for q_dep in queryset_dep:
            sum_queryset['dep_verification_count'] += q_dep['verification_count'] if q_dep['verification_count'] else 0
            sum_queryset['dep_standart_sum'] += q_dep['standart_sum'] if q_dep['standart_sum'] else 0

        result_queryset = []
        temp_dict = {'location_name': '',
                     'dep_verification_count': '',
                     'dep_standart_sum': '',
                     'dep_avg_rank': '',
                     'gov_verification_count': '',
                     'gov_standart_sum': '',
                     'gov_avg_rank': ''}
        for q_gov in queryset_gov:
            temp_dict['location_name'] = q_gov['location_name']
            temp_dict['gov_verification_count'] = q_gov['verification_count']
            temp_dict['gov_standart_sum'] = q_gov['standart_sum']
            temp_dict['gov_avg_rank'] = q_gov['avg_rank']
            for q_dep in queryset_dep:
                if q_gov['location_name'] == q_dep['location_name']:
                    temp_dict['dep_verification_count'] = q_dep['verification_count']
                    temp_dict['dep_standart_sum'] = q_dep['standart_sum']
                    temp_dict['dep_avg_rank'] = q_dep['avg_rank']
            result_queryset.append(temp_dict)
            temp_dict = {'location_name': '',
                         'dep_verification_count': '',
                         'dep_standart_sum': '',
                         'dep_avg_rank': '',
                         'gov_verification_count': '',
                         'gov_standart_sum': '',
                         'gov_avg_rank': ''}
        for q_dep in queryset_dep:
            if not any(d.get('location_name') == q_dep['location_name'] for d in result_queryset):
                temp_dict['location_name'] = q_dep['location_name']
                temp_dict['dep_verification_count'] = q_dep['verification_count']
                temp_dict['dep_standart_sum'] = q_dep['standart_sum']
                temp_dict['dep_avg_rank'] = q_dep['avg_rank']
                result_queryset.append(temp_dict)
                temp_dict = {'location_name': '',
                             'dep_verification_count': '',
                             'dep_standart_sum': '',
                             'dep_avg_rank': '',
                             'gov_verification_count': '',
                             'gov_standart_sum': '',
                             'gov_avg_rank': ''}

        context['start_date'] = start_date
        context['queryset'] = result_queryset
        context['period_is_month'] = True if period == 'month' else False
        context['sum_queryset'] = sum_queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = EconomVerifCostsPeriodForm()
        return render(request,
                      'references/modals/econom_verif_costs_period_modal.html',
                      {'form': form})
