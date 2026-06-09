from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels


class MocInStorageView(LoginRequiredMixin, TemplateView):
    """
        Сведения о СИ, находящихся на хранении
    """
    template_name = 'references/moc_in_storage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = pmodels.MocList.objects.select_related(
            'change_type',
            'moc_group').prefetch_related(
                'verification_info',
                'device_location').all().order_by('change_type__name')

        context['queryset'] = queryset
        return context
