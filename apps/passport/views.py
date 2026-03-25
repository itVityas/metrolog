from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch


class PassportDetailView(LoginRequiredMixin, ListView):
    """
        Passport Detail View
    """
    template_name = 'passport/passport_main.html'
    model = models.MocList
    paginate_by = 1

    def get_queryset(self):
        return models.MocList.objects.prefetch_related(
            'device_location',
            'verification_info',
            'repair_info',
            'device_status_date',
            'moc_metals').all()
