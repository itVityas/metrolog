from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import DeviceStatus
from ..forms import DeviceStatusForm
from django.http import HttpResponseRedirect


class DeviceStatusListView(LoginRequiredMixin, ListView):
    """
        ListView for DeviceStatus
    """
    model = DeviceStatus
    template_name = 'handbooks/tables/device_status_table.html'
    form = DeviceStatusForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = DeviceStatusForm
        return context


class DeviceStatusAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for DeviceStatus
    """
    model = DeviceStatus
    form_class = DeviceStatusForm
    success_url = reverse_lazy('device_status')


class DeviceStatusUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for DeviceStatus
    """
    model = DeviceStatus
    form_class = DeviceStatusForm
    success_url = reverse_lazy('device_status')


class DeviceStatusDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for DeviceStatus
    """
    model = DeviceStatus
    form_class = DeviceStatusForm
    success_url = reverse_lazy('device_status')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response
