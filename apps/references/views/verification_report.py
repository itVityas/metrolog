from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import OperatingTimeForm
from calendar import monthrange
from django.db.models import Count


class VerificationReportView(LoginRequiredMixin, TemplateView):
    """
        ОТЧЕТ по накопительным нарядам бюро поверки
    """
    template_name = 'references/verification_report.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = OperatingTimeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']

        _, num_days = monthrange(start_date.year, start_date.month)
        end_date = start_date.replace(day=num_days)

        queryset = pmodels.VerificationInfo.objects.prefetch_related(
            'moc_list'
                ).filter(
                    verification_date__range=[
                        start_date,
                        end_date]).exclude(
                            verification_sign__code='3').order_by(
                                'moc_list__change_type__code')

        result_list = []
        prev_change_type = None
        formatted_dict = {'change_type': '',
                          'total_sum_first': 0,
                          'total_sum_final': 0,
                          'complexity_first': 0,
                          'complexity_final': 0}
        for q in queryset:
            if prev_change_type is None:
                prev_change_type = q.moc_list.change_type
            if prev_change_type != q.moc_list.change_type:
                result_list.append(formatted_dict)
                formatted_dict = {'change_type': '',
                                  'total_sum_first': 0,
                                  'total_sum_final': 0,
                                  'complexity_first': 0,
                                  'complexity_final': 0}
                prev_change_type = q.moc_list.change_type
            formatted_dict['change_type'] = prev_change_type.name
            if q.verification_sign.code == '1':
                formatted_dict['total_sum_first'] += 1
                formatted_dict['complexity_first'] += q.moc_list.moc_type.standart_verification if q.moc_list.moc_type.standart_verification else 0
            if q.verification_sign.code == '2':
                formatted_dict['total_sum_final'] += 1
                formatted_dict['complexity_final'] += q.moc_list.moc_type.standart_verification if q.moc_list.moc_type.standart_verification else 0
        result_list.append(formatted_dict)
        final_data_list = [
            {'work_name': '1. Ведомственная поверка СИ по видам измерений',
             'data': result_list},
            {'work_name': '2. Метрологическая экспертиза ТД',
             'data': None},
            {'work_name': '3. Метрологическая аттестация НКИА',
             'data': None},
            {'work_name': '4. Контроль уровней ВЧ сигнала',
             'data': None},
            {'work_name': '5. Метрологический надзор',
             'data': None},
            {'work_name': '6. Ведение делопроизводства и задачи АРМ - МЕТРОЛОГ',
             'data': None},
            {'work_name': '7. Работы, связанные с метрологическим обеспечением производства',
             'data': None},
        ]
        context['start_date'] = start_date
        context['work_list'] = final_data_list
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = OperatingTimeForm()
        return render(request,
                      'references/modals/verification_report_modal.html',
                      {'form': form})
