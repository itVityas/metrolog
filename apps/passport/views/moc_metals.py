from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .. import models
from .. import forms
from django.http import HttpResponseRedirect


class MocMetalsCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for MocMetals
    """
    model = models.MocMetals
    form_class = forms.MocMetalsForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class MocMetalsUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for MocMetals
    """
    model = models.MocMetals
    form_class = forms.MocMetalsForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class MocMetalsDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for MocMetals
    """
    model = models.MocMetals
    form_class = forms.MocMetalsForm
    success_url = reverse_lazy('passport')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        response.status_code = 303
        return response
