from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .. import models
from .. import forms
from django.http import HttpResponseRedirect
from apps.handbooks import forms as h_forms
from apps.handbooks import models as h_models
from django.shortcuts import render
from django.views.generic.edit import BaseFormView


class DeviceStatusDateCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for DeviceStatusDate
    """
    model = models.DeviceStatusDate
    form_class = forms.DeviceStatusDateForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class DeviceStatusDateUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for DeviceStatusDate
    """
    model = models.DeviceStatusDate
    form_class = forms.DeviceStatusDateForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


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
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        response.status_code = 303
        return response


class PassportDeviceStatusView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new DeviceStatus
    """
    model = h_models.DeviceStatus
    form_class = h_forms.DeviceStatusForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.DeviceStatusDateForm()
        return render(request,
                      'passport/modals/moc_list_table_modal.html',
                      {'tform': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.DeviceStatusForm()
        return render(request,
                      'handbooks/modals/passport_table_modal.html',
                      {'form': form,
                       'modal_name': 'status',
                       'field_name': 'device_status'})
