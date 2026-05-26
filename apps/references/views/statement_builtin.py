from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from datetime import date


class StatementBuiltinView(LoginRequiredMixin, TemplateView):
    """
        Ведомость (для встроенных)
    """
    template_name = 'references/statement_builtin.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        start_date = date.today()
        start_date = start_date.replace(year=start_date.year - 2)
        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info',
                'device_location',
                'device_station').filter(
                        sign_o_m=pmodels.MocList.SignOM.BUILTIN
                        ).order_by('verification_type', 'change_type__name')

        context['queryset'] = queryset
        context['start_date'] = start_date
        return self.render_to_response(context)
