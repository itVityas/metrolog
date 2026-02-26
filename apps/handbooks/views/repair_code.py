from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import RepairCode
from ..forms import RepairCodeForm
from django.http import HttpResponseRedirect


class RepairCodeListView(LoginRequiredMixin, ListView):
    """
        ListView for RepairCode
    """
    model = RepairCode
    template_name = 'handbooks/tables/repair_code_table.html'
    form = RepairCodeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = RepairCodeForm
        return context


class RepairCodeAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for RepairCode
    """
    model = RepairCode
    form_class = RepairCodeForm
    success_url = reverse_lazy('repair_code')


class RepairCodeUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for RepairCode
    """
    model = RepairCode
    form_class = RepairCodeForm
    success_url = reverse_lazy('repair_code')


class RepairCodeDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for RepairCode
    """
    model = RepairCode
    form_class = RepairCodeForm
    success_url = reverse_lazy('repair_code')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response
