from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch


class PassportDetailView(LoginRequiredMixin, TemplateView):
    """
        Passport Detail View
    """
    template_name = 'passport/passport_main.html'
    # model = models.MocList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        device_location = models.DeviceLocation.objects.select_related('department')
        verification_info = models.VerificationInfo.objects.select_related('verification_person', 'verification_sign')

        moc_list = models.MocList.objects.prefetch_related(
            Prefetch('device_location',
                     queryset=device_location,
                     to_attr='department'),
            Prefetch('verification_info',
                     queryset=verification_info,
                     to_attr='verifications'),
        ).get(id=int(pk))
        print(moc_list.verifications[0].verification_person.fio)
        # verbose names in template
        verbose_names = {}
        for field in models.MocList._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['object'] = moc_list
        context['department'] = moc_list.department[-1].department
        return context
