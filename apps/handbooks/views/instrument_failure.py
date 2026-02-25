from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import InstrumentFailure
from ..forms import InstrumentFailureForm
from django.http import HttpResponseRedirect


class InstrumentFailureListView(LoginRequiredMixin, ListView):
    """
        ListView for InstrumentFailure
    """
    model = InstrumentFailure
    template_name = 'handbooks/tables/instrument_failure_table.html'
    form = InstrumentFailureForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = InstrumentFailureForm
        return context


class InstrumentFailureAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for InstrumentFailure
    """
    model = InstrumentFailure
    form_class = InstrumentFailureForm
    success_url = reverse_lazy('instrument_failure')


class InstrumentFailureUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for InstrumentFailure
    """
    model = InstrumentFailure
    form_class = InstrumentFailureForm
    success_url = reverse_lazy('instrument_failure')


class InstrumentFailureDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for InstrumentFailure
    """
    model = InstrumentFailure
    form_class = InstrumentFailureForm
    success_url = reverse_lazy('instrument_failure')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
