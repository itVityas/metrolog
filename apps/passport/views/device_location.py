from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .. import models
from .. import forms
from django.http import HttpResponseRedirect


class DeviceLocationCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for DeviceLocation
    """
    model = models.DeviceLocation
    form_class = forms.DeviceLocationForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class DeviceLocationUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for DeviceLocation
    """
    model = models.DeviceLocation
    form_class = forms.DeviceLocationForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class DeviceLocationDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for DeviceLocation
    """
    model = models.DeviceLocation
    form_class = forms.DeviceLocationForm
    success_url = reverse_lazy('passport')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        response.status_code = 303
        return response
