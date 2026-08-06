from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from ..forms import MocInUseForm
from django.shortcuts import render
from django.db.models import OuterRef, Subquery


class MocInUseView(LoginRequiredMixin, TemplateView):
    """
        Сведения о наличии типа СИ
    """
    template_name = 'references/moc_in_use.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        moc_name = request.POST.get('moc_name')

        latest_device_location_query = pmodels.DeviceLocation.objects.filter(
            moc_list=OuterRef('pk')
            ).order_by('-id')

        latest_verification_info_query = pmodels.VerificationInfo.objects.filter(
            moc_list=OuterRef('pk')
            ).exclude(
                verification_date=None,
                ).order_by('-id', '-verification_date')

        latest_device_status_query = pmodels.DeviceStatusDate.objects.filter(
            moc_list=OuterRef('pk')
            ).order_by('-id')

        queryset = pmodels.MocList.objects.select_related(
            'change_type',
            'moc_group',
            'moc_type').prefetch_related(
                'verification_info',
                'device_location',
                'device_status_date').annotate(
                    last_location_name=Subquery(
                        latest_device_location_query.values(
                            'department__name')[:1]),
                    last_verification_date=Subquery(
                        latest_verification_info_query.values(
                            'verification_date')[:1]),
                    last_device_status=Subquery(
                        latest_device_status_query.values(
                            'device_status__name')[:1]),
                    ).filter(
                        moc_type__type=moc_name).order_by(
                            'last_device_status',
                            'inv_number',)

        for item in queryset:
            if item.last_location_name == '"Исп.центр центр"':
                item.last_location_name = 'Исп.центр'
            if item.last_location_name == 'Тех.центр центр центр':
                item.last_location_name = 'Тех.центр'

        context['queryset'] = queryset
        context['moc_name'] = moc_name
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = MocInUseForm()
        return render(request,
                      'references/modals/moc_in_use_modal.html',
                      {'form': form})
