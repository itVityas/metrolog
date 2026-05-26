from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels


class MocInUseView(LoginRequiredMixin, TemplateView):
    """
        Сведения о наличии типа СИ
    """
    template_name = 'references/moc_in_use.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        moc_name = request.POST.get('moc_name')

        queryset = pmodels.MocList.objects.select_related(
            'change_type',
            'moc_group',
            'moc_type').prefetch_related(
                'verification_info',
                'device_location',
                'device_status_date').filter(moc_type__type=moc_name)

        context['queryset'] = queryset
        return self.render_to_response(context)
