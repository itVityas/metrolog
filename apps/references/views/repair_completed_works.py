from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import CompletedWorksForm
from django.db.models.functions import Extract
from django.db.models import Count, Sum
from django.db.models import F


class RepairCompletedWorksView(LoginRequiredMixin, TemplateView):
    """
        Ведомость выполненых работ для цеха за месяц
    """
    template_name = 'references/repair_completed_works.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = CompletedWorksForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']
            start_date = form.cleaned_data['start_date']

        queryset = pmodels.RepairInfo.objects.select_related(
            'moc_list').prefetch_related('moc_list__device_location').filter(
                    moc_list__device_location__department=department,
                    repair_date__year=Extract(start_date, 'year'),
                    repair_date__month=Extract(start_date, 'month')).values(
                        'moc_list__moc_group__name',
                        'moc_list__moc_type__type',
                        'moc_list__moc_type__rank_repair',
                        'moc_list__moc_type__standart_repair',
                        'moc_list__moc_type__cost',
                        'repair_code__code',
                        ).annotate(moc_count=Count('moc_list__moc_type'))

        sum_queryset = queryset.values('moc_list__moc_type__standart_repair', 'moc_count').aggregate(
            standart_sum=Sum(F('moc_list__moc_type__standart_repair') * F('moc_count')),
            moc_count_sum=Sum(F('moc_count')),
            )

        context['department'] = department.name
        context['start_date'] = start_date
        context['queryset'] = queryset
        context['sum_queryset'] = sum_queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = CompletedWorksForm()
        return render(request,
                      'references/modals/repair_completed_works_modal.html',
                      {'form': form})
