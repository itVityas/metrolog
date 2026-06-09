from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from datetime import date
from django.db.models.functions import Extract
from django.db.models import OuterRef, Subquery


class StatementBuiltinView(LoginRequiredMixin, TemplateView):
    """
        Ведомость (для встроенных)
    """
    template_name = 'references/statement_builtin.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_verification_info_query = pmodels.VerificationInfo.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-verification_date')

        latest_device_location_query = pmodels.DeviceLocation.objects.filter(
            moc_list=OuterRef('pk')
        ).order_by('-entry_date')

        start_date = date.today()
        start_date = start_date.replace(year=start_date.year - 2)
        queryset = pmodels.MocList.objects.select_related(
            'moc_type',
            'moc_group').prefetch_related(
                'verification_info',
                'device_location',
                'device_station').annotate(
                    last_verification_date=Subquery(
                        latest_verification_info_query.values(
                            'verification_date')[:1]),
                    last_device_location=Subquery(
                        latest_device_location_query.values(
                            'department__name')[:1])).filter(
                                verification_period__lte=(
                                    Extract(start_date, 'year') -
                                    Extract('last_verification_date',
                                            'year')) * 12 +
                                (Extract(start_date, 'month') -
                                    Extract('last_verification_date',
                                            'month'))).filter(
                                                sign_o_m=pmodels.MocList.SignOM.BUILTIN
                                                ).order_by('verification_type',
                                                           'change_type__name')

        context['queryset'] = queryset
        context['start_date'] = start_date
        return self.render_to_response(context)
