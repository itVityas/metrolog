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


class PassportDepartmentView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new Department
    """
    model = h_models.Department
    form_class = h_forms.DepartmentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.DeviceLocationForm()
        return render(request,
                      'passport/modals/moc_list_table_modal.html',
                      {'tform': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.DepartmentForm()
        return render(request,
                      'handbooks/modals/passport_table_modal.html',
                      {'form': form,
                       'modal_name': 'location',
                       'field_name': 'department'})
