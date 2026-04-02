from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .. import models
from .. import forms
from django.http import HttpResponseRedirect


class VerificationInfoCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for VerificationInfo
    """
    model = models.VerificationInfo
    form_class = forms.VerificationInfoForm
    success_url = reverse_lazy('passport')


class VerificationInfoUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for VerificationInfo
    """
    model = models.VerificationInfo
    form_class = forms.VerificationInfoForm
    success_url = reverse_lazy('passport')


class VerificationInfoDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for VerificationInfo
    """
    model = models.VerificationInfo
    form_class = forms.VerificationInfoForm
    success_url = reverse_lazy('passport')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response
