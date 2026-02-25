from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import ChangeType
from ..forms import ChangeTypeForm
from django.http import HttpResponseRedirect


class ChangeTypeListView(LoginRequiredMixin, ListView):
    """
        ListView for ChangeType
    """
    model = ChangeType
    template_name = 'handbooks/tables/change_type_table.html'
    form = ChangeTypeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = ChangeTypeForm
        return context


class ChangeTypeAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for ChangeType
    """
    model = ChangeType
    form_class = ChangeTypeForm
    success_url = reverse_lazy('change_type')


class ChangeTypeUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for ChangeType
    """
    model = ChangeType
    form_class = ChangeTypeForm
    success_url = reverse_lazy('change_type')


class ChangeTypeDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for ChangeType
    """
    model = ChangeType
    form_class = ChangeTypeForm
    success_url = reverse_lazy('change_type')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())