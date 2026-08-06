from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.db.models import Count
from itertools import chain


class MocVerificationTypesView(LoginRequiredMixin, TemplateView):
    """
        Справка о количестве СИ по видам поверки
    """
    template_name = 'references/moc_verification_types.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = pmodels.MocList.objects.select_related(
            'change_type').values(
                'change_type__name', 'change_type__code').annotate(total=Count('id')).order_by('change_type__code')

        queryset_g_o = pmodels.MocList.objects.select_related(
            'change_type').filter(
                verification_type='Г',
                sign_o_r='О').values(
                    'change_type__name', 'change_type__code').annotate(count_g_o=Count('id'))

        queryset_g_r = pmodels.MocList.objects.select_related(
            'change_type').filter(
                verification_type='Г',
                sign_o_r='Р').values(
                    'change_type__name', 'change_type__code').annotate(count_g_r=Count('id'))

        queryset_v_r = pmodels.MocList.objects.select_related(
            'change_type').filter(
                verification_type='В',
                sign_o_r='Р').values(
                    'change_type__name', 'change_type__code').annotate(count_v_r=Count('id'))

        all_dicts = chain(queryset, queryset_v_r, queryset_g_o, queryset_g_r)
        merged_data = {}
        for item in all_dicts:
            key = item['change_type__name']
            if key in merged_data:
                merged_data[key].update(item)
            else:
                merged_data[key] = item

        total_count = 0
        for item in list(merged_data.values()):
            total_count += item['total']

        context['queryset'] = list(merged_data.values())
        context['total_count'] = total_count
        return context
