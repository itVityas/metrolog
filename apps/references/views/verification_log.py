from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import VerificationLogForm
from django.db.models.functions import Extract
from django.db.models import Sum,  OuterRef, Subquery


class VerificationLogView(LoginRequiredMixin, TemplateView):
    """
        Журнал поверки
    """
    template_name = 'references/verification_log.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = VerificationLogForm(request.POST)
        if form.is_valid():
            change_type = form.cleaned_data['change_type']
            start_date = form.cleaned_data['start_date']

        latest_verification_info_query = pmodels.VerificationInfo.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-verification_date')

        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').annotate(
                last_verification_date=Subquery(
                    latest_verification_info_query.values(
                        'verification_date')[:1])
                ).filter(
                    change_type=change_type,
                    verification_period__lt=(
                        Extract(start_date, 'year') -
                        Extract('last_verification_date',
                                'year')) * 12 +
                    (Extract(start_date, 'month') -
                        Extract('last_verification_date',
                                'month'))).order_by(
                                    'device_location__department')

        verif_queryset = pmodels.VerificationInfo.objects.select_related(
            'moc_list').prefetch_related(
                'moc_list__device_location',).filter(
                    moc_list__change_type=change_type,
                    moc_list__verification_period__lt=(
                        Extract(start_date, 'year') -
                        Extract('verification_date',
                                'year')) * 12 +
                    (Extract(start_date, 'month') -
                        Extract('verification_date',
                                'month'))).order_by(
                                    'moc_list__device_location__department')

        queryset_count = queryset.values(
            'device_location__department').annotate(
                sum_standart_verif=Sum(
                    'moc_type__standart_verification'))

        print(verif_queryset)
        context['start_date'] = start_date
        context['queryset'] = queryset
        context['queryset_count'] = dict(queryset_count)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = VerificationLogForm()
        return render(request,
                      'references/modals/verification_log_modal.html',
                      {'form': form})
