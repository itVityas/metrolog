from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import PreciousMetals
from ..forms import PreciousMetalsForm
from django.http import HttpResponseRedirect


class PreciousMetalsListView(LoginRequiredMixin, ListView):
    """
        ListView for PreciousMetals
    """
    model = PreciousMetals
    template_name = 'handbooks/tables/precious_metals_table.html'
    form = PreciousMetalsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = PreciousMetalsForm
        return context


class PreciousMetalsAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for PreciousMetals
    """
    model = PreciousMetals
    form_class = PreciousMetalsForm
    success_url = reverse_lazy('precious_metals')


class PreciousMetalsUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for PreciousMetals
    """
    model = PreciousMetals
    form_class = PreciousMetalsForm
    success_url = reverse_lazy('precious_metals')


class PreciousMetalsDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for PreciousMetals
    """
    model = PreciousMetals
    form_class = PreciousMetalsForm
    success_url = reverse_lazy('precious_metals')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
