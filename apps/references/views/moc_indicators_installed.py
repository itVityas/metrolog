from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import MocIndicatorsForm


class MocIndicatorsInstalledView(LoginRequiredMixin, TemplateView):
    """
        Перечень СИ, переведенных в индикаторы
    """
    template_name = 'references/moc_indicators_installed.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = MocIndicatorsForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group',
            'change_type').prefetch_related(
                'verification_info',
                'device_location',
                'device_station').filter(
                    device_location__department=department,
                    change_type__code='99/3')

        context['department'] = department.name
        context['queryset'] = queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = MocIndicatorsForm()
        return render(request,
                      'references/modals/moc_indicators_installed_modal.html',
                      {'form': form})
