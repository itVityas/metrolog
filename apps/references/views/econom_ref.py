from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import EconomRefForm
from django.db.models.functions import Extract
from django.db.models import Count, Sum, Avg
from django.db.models import F


class EconomRefView(LoginRequiredMixin, TemplateView):
    """
        Справка о трудоемкости работ по видам измерений
    """
    template_name = 'references/econom_ref.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = EconomRefForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']

        queryset_gov = pmodels.VerificationInfo.objects.select_related(
            'moc_list').prefetch_related('moc_list__device_location').filter(
                verification_date__year=Extract(start_date, 'year'),
                moc_list__verification_type=pmodels.MocList.VerificationType.GOVERNMENTAL).values(
                    change_type=F('moc_list__change_type__name'),
                    ).annotate(
                        verification_count=Count('moc_list__moc_type'),
                        standart_sum=Sum('moc_list__moc_type__standart_verification'),
                        avg_rank=Avg('moc_list__moc_type__rank_verification')
                        ).order_by('change_type')
        queryset_dep = pmodels.VerificationInfo.objects.select_related(
            'moc_list').prefetch_related('moc_list__device_location').filter(
                verification_date__year=Extract(start_date, 'year'),
                moc_list__verification_type=pmodels.MocList.VerificationType.DEPARTMENTAL).values(
                    change_type=F('moc_list__change_type__name'),
                    ).annotate(
                        verification_count=Count('moc_list__moc_type'),
                        standart_sum=Sum('moc_list__moc_type__standart_verification'),
                        avg_rank=Avg('moc_list__moc_type__rank_verification')
                        ).order_by('change_type')

        result_list = []
        verification_count = 0
        standart_sum = 0
        list_to_add = []
        for q in queryset_dep:
            verification_count += q['verification_count'] if q['verification_count'] is not None else 0
            standart_sum += q['standart_sum'] if q['standart_sum'] is not None else 0
            list_to_add.append(q)
        result_list.append({'verification_type': 'Ведомственная',
                            'verification_count': verification_count,
                            'standart_sum': standart_sum,
                            'values': list_to_add})
        verification_count = 0
        standart_sum = 0
        list_to_add = []
        for q in queryset_gov:
            verification_count += q['verification_count'] if q['verification_count'] is not None else 0
            standart_sum += q['standart_sum'] if q['standart_sum'] is not None else 0
            list_to_add.append(q)
        result_list.append({'verification_type': 'Государственная',
                            'verification_count': verification_count,
                            'standart_sum': standart_sum,
                            'values': list_to_add})

        context['start_date'] = start_date
        context['queryset'] = result_list
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = EconomRefForm()
        return render(request,
                      'references/modals/econom_ref_modal.html',
                      {'form': form})
