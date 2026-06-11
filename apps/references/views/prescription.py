from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
import datetime
from ..forms import MemorandumForm
from django.shortcuts import render
from django.db.models.functions import Extract
from django.db.models import OuterRef, Subquery


class PrescriptionView(LoginRequiredMixin, TemplateView):
    """
        Предписание (кроме встроенных)
    """
    template_name = 'references/prescription.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_verification_info_query = pmodels.VerificationInfo.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-verification_date')

        form = MemorandumForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            workshop = form.cleaned_data['workshop']
            brigade = form.cleaned_data['brigade']

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info').annotate(
                    last_verification_date=Subquery(
                        latest_verification_info_query.values(
                            'verification_date')[:1]),).filter(
                                last_verification_date__lte=start_date,
                                device_location__department__workshop=workshop,
                                device_location__department__brigade=brigade).exclude(
                                    sign_o_m=pmodels.MocList.SignOM.BUILTIN
                                    ).order_by('verification_type', 'change_type')

        context['queryset'] = queryset
        context['start_date'] = start_date
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = MemorandumForm()
        return render(request,
                      'references/modals/prescription_modal.html',
                      {'form': form})
