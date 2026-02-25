from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import VerificationPerson
from ..forms import VerificationPersonForm
from django.http import HttpResponseRedirect


class VerificationPersonListView(LoginRequiredMixin, ListView):
    """
        ListView for VerificationPerson
    """
    model = VerificationPerson
    template_name = 'handbooks/tables/verification_person_table.html'
    form = VerificationPersonForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = VerificationPersonForm
        return context


class VerificationPersonAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for VerificationPerson
    """
    model = VerificationPerson
    form_class = VerificationPersonForm
    success_url = reverse_lazy('verification_person')


class VerificationPersonUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for VerificationPerson
    """
    model = VerificationPerson
    form_class = VerificationPersonForm
    success_url = reverse_lazy('verification_person')


class VerificationPersonDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for VerificationPerson
    """
    model = VerificationPerson
    form_class = VerificationPersonForm
    success_url = reverse_lazy('verification_person')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
