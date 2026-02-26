from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import RepairDepartment
from ..forms import RepairDepartmentForm
from django.http import HttpResponseRedirect


class RepairDepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for RepairDepartment
    """
    model = RepairDepartment
    template_name = 'handbooks/tables/repair_department_table.html'
    form = RepairDepartmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = RepairDepartmentForm
        return context


class RepairDepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')


class RepairDepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')


class RepairDepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response
