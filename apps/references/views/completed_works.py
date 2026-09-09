from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import CompletedWorksForm
from django.db.models.functions import Extract
from django.db.models import Count, Sum
from django.db.models import F
from django.db.models import OuterRef, Subquery
from collections import Counter
from decimal import Decimal


class CompletedWorksView(LoginRequiredMixin, TemplateView):
    """
        Ведомость выполненых работ по поверке для цеха
    """
    template_name = 'references/completed_works.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_device_location_query = pmodels.DeviceLocation.objects.filter(
            moc_list=OuterRef('pk')
            ).order_by('-id')

        latest_verification_info_query = pmodels.VerificationInfo.objects.filter(
            moc_list=OuterRef('pk')
            ).exclude(
                verification_date=None,
                ).order_by('-entry_date')

        latest_device_status_query = pmodels.DeviceStatusDate.objects.filter(
            moc_list=OuterRef('pk')
            ).order_by('-id')

        form = CompletedWorksForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']
            start_date = form.cleaned_data['start_date']

        queryset = pmodels.MocList.objects.select_related(
            'moc_type').prefetch_related('verification_info').annotate(
                    verification_date=Subquery(
                        latest_verification_info_query.filter(
                            verification_date__year=Extract(start_date, 'year'),
                            verification_date__month=Extract(start_date, 'month')).values(
                                'verification_date')[:1]),
                    last_location=Subquery(
                        latest_device_location_query.values(
                            'department')[:1]),
                    last_verification_date=Subquery(
                        latest_verification_info_query.values(
                            'verification_date')[:1]),
                    last_device_status=Subquery(
                        latest_device_status_query.values(
                            'device_status__name')[:1]),
                    ).filter(
                        last_location=department).exclude(
                            verification_date=None
                            ).values(
                                'inv_number',
                                'moc_group__name',
                                'verification_date',
                                'moc_type__type',
                                'moc_type__rank_verification',
                                'moc_type__standart_verification'
                                ).order_by(
                                    'moc_type__type'
                                )

        if department.name == '"Исп.центр центр"':
            department.name = 'Исп.центр'
        if department.name == 'Тех.центр центр центр':
            department.name = 'Тех.центр'

        result_queryset = []
        temp_list = []
        prev_type = None
        for q in queryset:
            if prev_type is None:
                prev_type = q
            if prev_type['moc_type__type'] == q['moc_type__type']:
                temp_list.append(q['inv_number'])
                prev_type = q
            else:
                result_queryset.append({
                    'name': prev_type['moc_group__name'],
                    'verification_date': prev_type['verification_date'],
                    'type': prev_type['moc_type__type'],
                    'rank_verification': prev_type['moc_type__rank_verification'],
                    'standart_verification': prev_type['moc_type__standart_verification'],
                    'inv_num_list': temp_list.copy()
                })
                temp_list.clear()
                temp_list.append(q['inv_number'])
                prev_type = q
        if prev_type:
            result_queryset.append({
                    'name': prev_type['moc_group__name'],
                    'verification_date': prev_type['verification_date'],
                    'type': prev_type['moc_type__type'],
                    'rank_verification': prev_type['moc_type__rank_verification'],
                    'standart_verification': prev_type['moc_type__standart_verification'],
                    'inv_num_list': temp_list.copy()
                })
        temp_list.clear()

        sum_queryset = {'total_amount': len(queryset),
                        'standart_sum': sum(item['moc_type__standart_verification'] if item['moc_type__standart_verification'] is not None else Decimal('0') for item in queryset)}

        context['department'] = department.name
        context['start_date'] = start_date
        context['queryset'] = result_queryset
        context['sum_queryset'] = sum_queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = CompletedWorksForm()
        return render(request,
                      'references/modals/completed_works_modal.html',
                      {'form': form})
