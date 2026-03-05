from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import RepairDepartment
from ..forms import RepairDepartmentForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class RepairDepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for RepairDepartment
    """
    model = RepairDepartment
    template_name = 'handbooks/tables/repair_department_table.html'
    form = RepairDepartmentForm
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
        context['form'] = RepairDepartmentForm
        return context


class RepairDepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')


class RepairDepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')


class RepairDepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class RepairDepartmentMigrateView(LoginRequiredMixin, View):
    model = RepairDepartment
    success_url = reverse_lazy('repair_department')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb016.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['code'] = record.get('KOD_REM')
            new_dict['sign'] = record.get('RAZR')
            new_dict['name'] = record.get('FIO')
            new_dict['is_active'] = True
            data_list.append(new_dict)

        obj_list = [RepairDepartment(**data_dict) for data_dict in data_list]
        RepairDepartment.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
