from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import MocGroup
from ..forms import MocGroupForm
from django.http import HttpResponseRedirect


class MocGroupListView(LoginRequiredMixin, ListView):
    """
        ListView for MocGroup
    """
    model = MocGroup
    template_name = 'handbooks/tables/moc_group_table.html'
    form = MocGroupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = MocGroupForm
        return context


class MocGroupAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for MocGroup
    """
    model = MocGroup
    form_class = MocGroupForm
    success_url = reverse_lazy('moc_group')


class MocGroupUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for MocGroup
    """
    model = MocGroup
    form_class = MocGroupForm
    success_url = reverse_lazy('moc_group')


class MocGroupDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for MocGroup
    """
    model = MocGroup
    form_class = MocGroupForm
    success_url = reverse_lazy('moc_group')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response
