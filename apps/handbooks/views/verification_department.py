from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import VerificationDepartment
from ..forms import VerificationDepartmentForm
from django.http import HttpResponseRedirect


class VerificationDepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for VerificationDepartment
    """
    model = VerificationDepartment
    template_name = 'handbooks/tables/verification_department_table.html'
    form = VerificationDepartmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = VerificationDepartmentForm
        return context


class VerificationDepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for VerificationDepartment
    """
    model = VerificationDepartment
    form_class = VerificationDepartmentForm
    success_url = reverse_lazy('verification_department')


class VerificationDepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for VerificationDepartment
    """
    model = VerificationDepartment
    form_class = VerificationDepartmentForm
    success_url = reverse_lazy('verification_department')


class VerificationDepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for VerificationDepartment
    """
    model = VerificationDepartment
    form_class = VerificationDepartmentForm
    success_url = reverse_lazy('verification_department')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response
