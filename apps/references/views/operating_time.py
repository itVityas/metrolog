from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import VerificationOperatingTimeForm
from calendar import monthrange
from django.db.models.functions import Extract
from decimal import Decimal


class OperatingTimeView(LoginRequiredMixin, TemplateView):
    """
        Накопительная наработка прибориста
    """
    template_name = 'references/operating_time.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = VerificationOperatingTimeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            verif_person = form.cleaned_data['person']
            for_all = form.cleaned_data['for_all']

        if for_all:
            queryset = pmodels.VerificationInfo.objects.prefetch_related(
                'moc_list'
                    ).filter(
                        verification_date__year=Extract(start_date, 'year'),
                        verification_date__month=Extract(start_date, 'month')).order_by(
                            'verification_person',
                            'moc_list__moc_type__type')
        else:
            queryset = pmodels.VerificationInfo.objects.prefetch_related(
                'moc_list'
                    ).filter(
                        verification_person=verif_person,
                        verification_date__year=Extract(start_date, 'year'),
                        verification_date__month=Extract(start_date, 'month')).order_by(
                            'verification_person',
                            'moc_list__moc_type__type')

        result_list = []
        temp_list = []
        prev_repair_department = None
        ver_bool_result = False
        failure_code = None
        formatted_dict = {'repair_person': '',
                          'person_rank': '',
                          'sum_standart': 0,
                          'values_list': []}
        for q in queryset:
            if q.verification_result == '1':
                ver_bool_result = True
            else:
                failure_code = pmodels.RepairInfo.objects.select_related(
                    'instrument_failure'
                    ).prefetch_related(
                        'moc_list'
                        ).filter(
                            moc_list=q.moc_list,
                            entry_date=q.verification_date
                            ).values(
                                'instrument_failure__code'
                                ).first()
                failure_code = failure_code['instrument_failure__code']
            if prev_repair_department is None:
                prev_repair_department = q.verification_person
            if prev_repair_department != q.verification_person:
                formatted_dict['values_list'] = temp_list.copy()
                temp_list.clear()
                result_list.append(formatted_dict)
                formatted_dict = {'repair_person': '',
                                  'person_rank': '',
                                  'sum_standart': 0,
                                  'values_list': []}
                prev_repair_department = q.verification_person
            if prev_repair_department:
                formatted_dict['repair_person'] = prev_repair_department.fio
                formatted_dict['person_rank'] = prev_repair_department.rank
                formatted_dict['sum_standart'] += q.moc_list.moc_type.standart_verification
            temp_list.append({'result': ver_bool_result,
                              'values': q,
                              'failure_code': failure_code})
            failure_code = None
            ver_bool_result = False
        formatted_dict['values_list'] = temp_list
        result_list.append(formatted_dict)
        print(result_list)

        context['start_date'] = start_date
        context['queryset'] = result_list
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = VerificationOperatingTimeForm()
        return render(request,
                      'references/modals/operating_time_modal.html',
                      {'form': form})
