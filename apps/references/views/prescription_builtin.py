from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from datetime import datetime


class PrescriptionBuiltinView(LoginRequiredMixin, TemplateView):
    """
        Предписание (для встроенных)
    """
    template_name = 'references/prescription_builtin.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        workshop = request.POST.get('workshop')
        brigade = request.POST.get('brigade')
        start_date = request.POST.get('start_date')

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info').filter(
                    device_location__department__workshop=workshop,
                    device_location__department__brigade=brigade).exclude(
                        sign_o_m=pmodels.MocList.SignOM.BUILTIN
                        ).order_by('verification_type')

        context['queryset'] = queryset
        context['start_date'] = datetime.strptime(start_date, "%d.%m.%Y").date()
        return self.render_to_response(context)
