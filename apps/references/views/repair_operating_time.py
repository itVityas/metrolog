from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import RepairOperatingTimeForm
from django.db.models.functions import Extract
from decimal import Decimal


class RepairOperatingTimeView(LoginRequiredMixin, TemplateView):
    """
        Накопительный наряд
    """
    template_name = 'references/repair_operating_time.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = RepairOperatingTimeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            repair_person = form.cleaned_data['person']
            for_all = form.cleaned_data['for_all']

        if for_all:
            queryset = pmodels.RepairInfo.objects.prefetch_related(
                'moc_list'
                    ).filter(
                        repair_date__year=Extract(start_date, 'year'),
                        repair_date__month=Extract(start_date, 'month')).order_by(
                            'repair_department')
        else:
            queryset = pmodels.RepairInfo.objects.prefetch_related(
                'moc_list'
                    ).filter(
                        repair_department=repair_person,
                        repair_date__year=Extract(start_date, 'year'),
                        repair_date__month=Extract(start_date, 'month')).order_by(
                            'repair_department')

        result_list = []
        temp_list = []
        prev_repair_department = None
        formatted_dict = {'repair_person': '',
                          'person_rank': '',
                          'sum_standart': 0,
                          'sum_salary': 0,
                          'values_list': []}
        for q in queryset:
            if prev_repair_department is None:
                prev_repair_department = q.repair_department
            if prev_repair_department != q.repair_department:
                formatted_dict['values_list'] = temp_list.copy()
                temp_list.clear()
                result_list.append(formatted_dict)
                formatted_dict = {'repair_person': '',
                                  'person_rank': '',
                                  'sum_standart': 0,
                                  'sum_salary': 0,
                                  'values_list': []}
                prev_repair_department = q.repair_department
            formatted_dict['repair_person'] = prev_repair_department.name
            formatted_dict['person_rank'] = prev_repair_department.sign
            formatted_dict['sum_standart'] += q.moc_list.moc_type.standart_repair
            formatted_dict['sum_salary'] = q.moc_list.moc_type.standart_repair * Decimal(str(0.9))
            temp_list.append(q)
        formatted_dict['values_list'] = temp_list
        result_list.append(formatted_dict)
        print(result_list)
        context['start_date'] = start_date
        context['queryset'] = result_list
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = RepairOperatingTimeForm()
        return render(request,
                      'references/modals/repair_operating_time_modal.html',
                      {'form': form})
