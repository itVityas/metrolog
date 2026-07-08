from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import OperatingTimeForm
from django.db.models.functions import Extract
from django.db.models import Count, Sum
from django.db.models import F


class RepairReportView(LoginRequiredMixin, TemplateView):
    """
        Отчет по нарядам
    """
    template_name = 'references/repair_report.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = OperatingTimeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']

        queryset = pmodels.RepairInfo.objects.select_related(
            'moc_list').prefetch_related('moc_list__device_location').filter(
                repair_date__year=Extract(start_date, 'year'),
                repair_date__month=Extract(start_date, 'month')).values(
                    'moc_list__change_type__name'
                    ).annotate(
                        moc_count=Count('moc_list__moc_type'),
                        sum_standart_repair=Sum('moc_list__moc_type__standart_repair')
                        )

        context['start_date'] = start_date
        context['queryset'] = queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = OperatingTimeForm()
        return render(request,
                      'references/modals/repair_report_modal.html',
                      {'form': form})
