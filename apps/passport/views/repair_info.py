from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .. import models
from .. import forms
from django.http import HttpResponseRedirect


class RepairInfoCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for RepairInfo
    """
    model = models.RepairInfo
    form_class = forms.RepairInfoForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class RepairInfoUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for RepairInfo
    """
    model = models.RepairInfo
    form_class = forms.RepairInfoForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class RepairInfoDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for RepairInfo
    """
    model = models.RepairInfo
    form_class = forms.RepairInfoForm
    success_url = reverse_lazy('passport')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        response.status_code = 303
        return response
