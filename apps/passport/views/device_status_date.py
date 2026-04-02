from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .. import models
from .. import forms
from django.http import HttpResponseRedirect


class DeviceStatusDateCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for DeviceStatusDate
    """
    model = models.DeviceStatusDate
    form_class = forms.DeviceStatusDateForm
    success_url = reverse_lazy('passport')


class DeviceStatusDateUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for DeviceStatusDate
    """
    model = models.DeviceStatusDate
    form_class = forms.DeviceStatusDateForm
    success_url = reverse_lazy('passport')


class DeviceStatusDateDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for DeviceStatusDate
    """
    model = models.DeviceStatusDate
    form_class = forms.DeviceStatusDateForm
    success_url = reverse_lazy('passport')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response
