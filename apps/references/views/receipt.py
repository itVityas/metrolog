from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import ReceiptForm
import datetime
from django.db.models.functions import Extract


class ReceiptView(LoginRequiredMixin, TemplateView):
    """
        Квитанция на получение СИ
    """
    template_name = 'references/receipt.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        today_date = datetime.date.today()
        form = ReceiptForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info').filter(
                    device_location__department=department,
                    verification_period__gte=(
                        Extract(today_date, 'year') -
                        Extract('verification_info__verification_date',
                                'year')) * 12 +
                    (Extract(today_date, 'month') -
                        Extract('verification_info__verification_date',
                                'month')))

        context['department'] = department.name
        context['queryset'] = queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = ReceiptForm()
        return render(request,
                      'references/modals/receipt_modal.html',
                      {'form': form})
