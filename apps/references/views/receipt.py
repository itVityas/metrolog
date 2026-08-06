from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import ReceiptForm
import datetime
from django.db.models.functions import Extract
from django.db.models import OuterRef, Subquery


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

        latest_verification_info_query = pmodels.VerificationInfo.objects.filter(
                    moc_list=OuterRef('pk')
                ).exclude(
                    verification_date=None,
                    ).order_by('-id', '-verification_date')

        latest_device_status_query = pmodels.DeviceStatusDate.objects.filter(
                    moc_list=OuterRef('pk')
                ).order_by('-id')

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info',
                'device_status_date').annotate(
                    last_workshop_issue_date=Subquery(
                        latest_verification_info_query.values(
                            'workshop_issue_date')[:1]),
                    last_verification_date=Subquery(
                        latest_verification_info_query.values(
                            'verification_date')[:1]),
                    last_device_status=Subquery(
                        latest_device_status_query.values(
                            'device_status__name')[:1]),
                    ).filter(
                        device_location__department=department,
                        last_workshop_issue_date=None,
                        last_device_status='В эксплуатации').order_by(
                            'moc_group__name'
                        )

        context['department'] = department.name
        context['queryset'] = queryset
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = ReceiptForm()
        return render(request,
                      'references/modals/receipt_modal.html',
                      {'form': form})
