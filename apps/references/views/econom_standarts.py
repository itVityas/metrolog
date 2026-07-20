from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import OperatingTimeForm
from django.db.models.functions import Extract
from django.db.models import OuterRef, Subquery
from django.db.models.functions import Extract
from django.db.models import F, Count, Sum, Avg
import datetime


class EconomStandartsView(LoginRequiredMixin, TemplateView):
    """
        НОРМЫ времени на поверку и ремонт средств измерения
    """
    template_name = 'references/econom_standarts.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        start_date = datetime.date.today()

        queryset_verif = pmodels.VerificationInfo.objects.select_related(
            'moc_list').prefetch_related('moc_list').filter(
                verification_date__year=Extract(start_date, 'year')
                ).values(
                    change_type=F('moc_list__change_type__name'),
                    moc_name=F('moc_list__moc_group__name'),
                    moc_type=F('moc_list__moc_type__type'),
                    rank_verification=F('moc_list__moc_type__rank_verification'),
                    standart_verification=F('moc_list__moc_type__standart_verification')
                    ).order_by('change_type')

        queryset_repair = pmodels.RepairInfo.objects.select_related(
            'moc_list').prefetch_related('moc_list').filter(
               repair_date__year=Extract(start_date, 'year')
               ).values(
                    change_type=F('moc_list__change_type__name'),
                    moc_name=F('moc_list__moc_group__name'),
                    moc_type=F('moc_list__moc_type__type'),
                    rank_repair=F('moc_list__moc_type__rank_repair'),
                    standart_repair=F('moc_list__moc_type__standart_repair'),
                    repair_code_is=F('repair_code__code')
                    ).order_by('change_type')

        result_queryset = []
        for q_ver in queryset_verif:
            for q_rep in queryset_repair:
                if q_ver['moc_type'] == q_rep['moc_type']:
                    result_queryset.append(q_ver | q_rep)
        for q_rep in queryset_repair:
            if not any(d.get('moc_type') == q_rep['moc_type'] for d in result_queryset):
                result_queryset.append(q_rep)

        context['start_date'] = start_date
        context['result_list'] = result_queryset
        return self.render_to_response(context)
