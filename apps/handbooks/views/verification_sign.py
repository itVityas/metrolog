from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import VerificationSign
from ..forms import VerificationSignForm
from django.http import HttpResponseRedirect


class VerificationSignListView(LoginRequiredMixin, ListView):
    """
        ListView for VerificationSign
    """
    model = VerificationSign
    template_name = 'handbooks/tables/verification_sign_table.html'
    form = VerificationSignForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = VerificationSignForm
        return context


class VerificationSignAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for VerificationSign
    """
    model = VerificationSign
    form_class = VerificationSignForm
    success_url = reverse_lazy('verification_sign')


class VerificationSignUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for VerificationSign
    """
    model = VerificationSign
    form_class = VerificationSignForm
    success_url = reverse_lazy('verification_sign')


class VerificationSignDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for VerificationSign
    """
    model = VerificationSign
    form_class = VerificationSignForm
    success_url = reverse_lazy('verification_sign')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
