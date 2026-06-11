from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
import datetime
from ..forms import MemorandumForm
from django.shortcuts import render
from calendar import monthrange


class MemorandumView(LoginRequiredMixin, TemplateView):
    """
        Служебная записка (кроме встроенных)
    """
    template_name = 'references/memorandum.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = MemorandumForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            workshop = form.cleaned_data['workshop']
            brigade = form.cleaned_data['brigade']

        _, num_days = monthrange(start_date.year, start_date.month)
        end_date = start_date.replace(day=num_days)

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info',
                'device_location').filter(
                    device_location__department__workshop=workshop,
                    device_location__department__brigade=brigade,
                    verification_info__verification_date__range=[
                        start_date,
                        end_date]).exclude(
                            sign_o_m=pmodels.MocList.SignOM.BUILTIN
                            ).order_by('verification_type')

        context['queryset'] = queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = MemorandumForm()
        return render(request,
                      'references/modals/memorandum_modal.html',
                      {'form': form})
