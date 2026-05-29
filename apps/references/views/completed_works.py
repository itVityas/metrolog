from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import CompletedWorksForm
from django.db.models.functions import Extract
from django.db.models import Count, Sum
from django.db.models import F


class CompletedWorksView(LoginRequiredMixin, TemplateView):
    """
        Ведомость выполненых работ по поверке для цеха
    """
    template_name = 'references/completed_works.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = CompletedWorksForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']
            start_date = form.cleaned_data['start_date']

        queryset = pmodels.VerificationInfo.objects.select_related(
            'moc_list').prefetch_related('moc_list__device_location').filter(
                    moc_list__device_location__department=department,
                    verification_date__year=Extract(start_date, 'year'),
                    verification_date__month=Extract(start_date, 'month')).values(
                        'moc_list__moc_group__name',
                        'moc_list__moc_type__type',
                        'moc_list__moc_type__rank_verification',
                        'moc_list__moc_type__standart_verification',
                        'moc_list__moc_type__cost',
                        ).annotate(moc_count=Count('moc_list__moc_type'))

        sum_queryset = queryset.values('moc_list__moc_type__standart_verification', 'moc_count').aggregate(
            standart_sum=Sum(F('moc_list__moc_type__standart_verification') * F('moc_count')),
            moc_count_sum=Sum(F('moc_count')),
            cost_sum=Sum(F('moc_list__moc_type__cost') * F('moc_count')),
            )

        context['department'] = department.name
        context['start_date'] = start_date
        context['queryset'] = queryset
        context['sum_queryset'] = sum_queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = CompletedWorksForm()
        return render(request,
                      'references/modals/completed_works_modal.html',
                      {'form': form})
