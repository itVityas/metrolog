from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Repair
from ..forms import RepairForm
from django.http import HttpResponseRedirect


class RepairListView(LoginRequiredMixin, ListView):
    """
        ListView for Repair
    """
    model = Repair
    template_name = 'handbooks/tables/repair_table.html'
    form = RepairForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = RepairForm
        return context


class RepairAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for Repair
    """
    model = Repair
    form_class = RepairForm
    success_url = reverse_lazy('repair')


class RepairUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for Repair
    """
    model = Repair
    form_class = RepairForm
    success_url = reverse_lazy('repair')


class RepairDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for Repair
    """
    model = Repair
    form_class = RepairForm
    success_url = reverse_lazy('repair')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
