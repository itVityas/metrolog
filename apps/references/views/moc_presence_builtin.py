from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from ...handbooks import models as hmodels
from django.shortcuts import render
from ..forms import MocPresenceForm


class MocPresenceBuiltinView(LoginRequiredMixin, TemplateView):
    """
        Наличие СИ в подразделении (для встроенных)
    """
    template_name = 'references/moc_presence_builtin.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = MocPresenceForm(request.POST)
        if form.is_valid():
            change_type = form.cleaned_data['change_type']
            department = form.cleaned_data['department']

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info',
                'device_location',
                'device_station',
                'device_status_date').filter(
                    change_type=change_type,
                    device_location__department=department,
                    sign_o_m=pmodels.MocList.SignOM.BUILTIN).order_by(
                        'verification_type',
                        'change_type__name')

        context['department'] = department.name
        context['queryset'] = queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = MocPresenceForm()
        return render(request,
                      'references/modals/moc_presence_builtin_modal.html',
                      {'form': form})
