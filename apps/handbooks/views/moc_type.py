from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import MocType
from ..forms import MocTypeForm
from django.http import HttpResponseRedirect


class MocTypeListView(LoginRequiredMixin, ListView):
    """
        ListView for MocType
    """
    model = MocType
    template_name = 'handbooks/tables/moc_type_table.html'
    form = MocTypeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = MocTypeForm
        return context


class MocTypeAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for MocType
    """
    model = MocType
    form_class = MocTypeForm
    success_url = reverse_lazy('moc_type')


class MocTypeUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for MocType
    """
    model = MocType
    form_class = MocTypeForm
    success_url = reverse_lazy('moc_type')


class MocTypeDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for MocType
    """
    model = MocType
    form_class = MocTypeForm
    success_url = reverse_lazy('moc_type')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
