from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import EconomVerifStandartsForm
from django.db.models.functions import Extract
from django.db.models import F, Count, Sum, Avg


class EconomVerifStandartsView(LoginRequiredMixin, TemplateView):
    """
        Справка о трудоемкости поверочных работ по цеху
    """
    template_name = 'references/econom_verif_standarts.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = EconomVerifStandartsForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            department = form.cleaned_data['department']
            period = form.cleaned_data['period']

        match period:
            case 'month':
                queryset = pmodels.VerificationInfo.objects.select_related(
                    'moc_list').prefetch_related('moc_list__device_location').filter(
                        verification_date__year=Extract(start_date, 'year'),
                        verification_date__month=Extract(start_date, 'month'),
                        moc_list__device_location__department=department).values(
                            moc_name=F('moc_list__moc_group__name'),
                            moc_type=F('moc_list__moc_type__type'),
                            verification_type=F('moc_list__verification_type'),
                            ).annotate(
                                verification_count=Count('moc_list__moc_type'),
                                standart_sum=Sum('moc_list__moc_type__standart_verification'),
                                avg_rank=Avg('moc_list__moc_type__rank_verification')
                                ).order_by('verification_type')
            case 'year':
                queryset = pmodels.VerificationInfo.objects.select_related(
                    'moc_list').prefetch_related('moc_list__device_location').filter(
                        verification_date__year=Extract(start_date, 'year'),
                        moc_list__device_location__department=department).values(
                            moc_name=F('moc_list__moc_group__name'),
                            moc_type=F('moc_list__moc_type__type'),
                            verification_type=F('moc_list__verification_type'),
                            ).annotate(
                                verification_count=Count('moc_list__moc_type'),
                                standart_sum=Sum('moc_list__moc_type__standart_verification'),
                                avg_rank=Avg('moc_list__moc_type__rank_verification')
                                ).order_by('verification_type')

        sum_queryset = {
            'verification_count': 0,
            'standart_sum': 0,
        }
        for q in queryset:
            sum_queryset['verification_count'] += q['verification_count'] if q['verification_count'] else 0
            sum_queryset['standart_sum'] += q['standart_sum'] if q['standart_sum'] else 0
            q['verification_type'] = pmodels.MocList.VerificationType(q['verification_type']).label

        context['start_date'] = start_date
        context['queryset'] = queryset
        context['period_is_month'] = True if period == 'month' else False
        context['sum_queryset'] = sum_queryset
        context['department'] = department
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = EconomVerifStandartsForm()
        return render(request,
                      'references/modals/econom_verif_standarts_modal.html',
                      {'form': form})
