from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Department
from ..forms import DepartmentForm
from django.http import HttpResponseRedirect


class DepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for Department
    """
    model = Department
    template_name = 'handbooks/tables/department_table.html'
    form = DepartmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = DepartmentForm
        return context


class DepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for Department
    """
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department')


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for Department
    """
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department')


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for Department
    """
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
