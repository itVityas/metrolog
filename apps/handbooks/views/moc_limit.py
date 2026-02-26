from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import MocLimit
from ..forms import MocLimitForm
from django.http import HttpResponseRedirect


class MocLimitListView(LoginRequiredMixin, ListView):
    """
        ListView for MocLimit
    """
    model = MocLimit
    template_name = 'handbooks/tables/moc_limit_table.html'
    form = MocLimitForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = MocLimitForm
        return context


class MocLimitAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for MocLimit
    """
    model = MocLimit
    form_class = MocLimitForm
    success_url = reverse_lazy('moc_limit')


class MocLimitUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for MocLimit
    """
    model = MocLimit
    form_class = MocLimitForm
    success_url = reverse_lazy('moc_limit')


class MocLimitDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for MocLimit
    """
    model = MocLimit
    form_class = MocLimitForm
    success_url = reverse_lazy('moc_limit')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response
