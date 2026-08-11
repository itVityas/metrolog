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

        result_queryset = pmodels.MocList.objects.filter(
                # verification_date__year=Extract(start_date, 'year')
                ).values(
                    change_type_name=F('change_type__name'),
                    moc_name=F('moc_group__name'),
                    moc_type_type=F('moc_type__type'),
                    rank_verification=F('moc_type__rank_verification'),
                    standart_verification=F('moc_type__standart_verification'),
                    rank_repair=F('moc_type__rank_repair'),
                    standart_repair=F('moc_type__standart_repair')
                    ).order_by('change_type__code')

        context['start_date'] = start_date
        context['result_list'] = result_queryset
        return self.render_to_response(context)
