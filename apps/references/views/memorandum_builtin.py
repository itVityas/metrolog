from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
import datetime


class MemorandumBuiltinView(LoginRequiredMixin, TemplateView):
    """
        Служебная записка (для встроенных)
    """
    template_name = 'references/memorandum_builtin.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        workshop = request.POST.get('workshop')
        brigade = request.POST.get('brigade')
        start_date = datetime.datetime.strptime(
            request.POST.get('start_date'),
            "%d.%m.%Y")
        end_date = start_date + datetime.timedelta(days=30)
        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info',
                'device_location',
                'device_station').filter(
                    device_location__department__workshop=workshop,
                    device_location__department__brigade=brigade,
                    verification_info__verification_date__range=[start_date,
                                                                 end_date],
                    sign_o_m=pmodels.MocList.SignOM.BUILTIN
                    ).order_by('verification_type')

        context['queryset'] = queryset
        return self.render_to_response(context)
