from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import UnitsMeasurement
from ..forms import UnitsMeasurementForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class UnitsMeasurementListView(LoginRequiredMixin, ListView):
    """
        ListView for UnitsMeasurement
    """
    model = UnitsMeasurement
    template_name = 'handbooks/tables/units_measurement_table.html'
    form = UnitsMeasurementForm
    paginate_by = settings.DEFAULT_PAGE_SIZE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # paginaton, deal wih too many pages
        page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(
            page.number, on_each_side=2, on_ends=1
        )
        # verbose names in template
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

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class UnitsMeasurementMigrateView(LoginRequiredMixin, View):
    model = UnitsMeasurement
    success_url = reverse_lazy('units_measurement')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb009.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['code'] = record.get('KOD')
            new_dict['name'] = record.get('NAME_ED')
            data_list.append(new_dict)

        obj_list = [UnitsMeasurement(**data_dict) for data_dict in data_list]
        UnitsMeasurement.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
