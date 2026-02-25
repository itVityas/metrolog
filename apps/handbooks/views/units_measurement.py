from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import UnitsMeasurement
from ..forms import UnitsMeasurementForm
from django.http import HttpResponseRedirect


class UnitsMeasurementListView(LoginRequiredMixin, ListView):
    """
        ListView for UnitsMeasurement
    """
    model = UnitsMeasurement
    template_name = 'handbooks/tables/units_measurement_table.html'
    form = UnitsMeasurementForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = UnitsMeasurementForm
        return context


class UnitsMeasurementAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for UnitsMeasurement
    """
    model = UnitsMeasurement
    form_class = UnitsMeasurementForm
    success_url = reverse_lazy('units_measurement')


class UnitsMeasurementUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for UnitsMeasurement
    """
    model = UnitsMeasurement
    form_class = UnitsMeasurementForm
    success_url = reverse_lazy('units_measurement')


class UnitsMeasurementDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for UnitsMeasurement
    """
    model = UnitsMeasurement
    form_class = UnitsMeasurementForm
    success_url = reverse_lazy('units_measurement')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
