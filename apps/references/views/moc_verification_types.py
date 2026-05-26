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
                'change_type__name').annotate(total=Count('id'))

        queryset_g_o = pmodels.MocList.objects.select_related(
            'change_type').filter(
                verification_type='Г',
                sign_o_r='О').values(
                    'change_type__name').annotate(count_g_o=Count('sign_o_r'))

        queryset_g_r = pmodels.MocList.objects.select_related(
            'change_type').filter(
                verification_type='Г',
                sign_o_r='Р').values(
                    'change_type__name').annotate(count_g_r=Count('sign_o_r'))

        queryset_v_r = pmodels.MocList.objects.select_related(
            'change_type').filter(
                verification_type='В',
                sign_o_r='Р').values(
                    'change_type__name').annotate(count_v_r=Count('sign_o_r'))

        all_dicts = chain(queryset, queryset_v_r, queryset_g_o, queryset_g_r)
        merged_data = {}
        for item in all_dicts:
            key = item['change_type__name']
            if key in merged_data:
                merged_data[key].update(item)
            else:
                merged_data[key] = item

        context['queryset'] = list(merged_data.values())
        return context
