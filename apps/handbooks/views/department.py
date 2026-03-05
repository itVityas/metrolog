from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Department
from ..forms import DepartmentForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class DepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for Department
    """
    model = Department
    template_name = 'handbooks/tables/department_table.html'
    form = DepartmentForm
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
        context['form'] = DepartmentForm
        return context


class DepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for Department
    """
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department')

    def post(self, request, *args, **kwargs):
        print(request.body)
        return super().post(request, *args, **kwargs)


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for Department
    """
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department')


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for Department
    """
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class DepartmentMigrateView(LoginRequiredMixin, View):
    model = Department
    success_url = reverse_lazy('department')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb002.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['workshop'] = record.get('CEX')
            new_dict['brigade'] = record.get('BR')
            new_dict['name'] = record.get('NKP')
            new_dict['is_active'] = True
            data_list.append(new_dict)

        obj_list = [Department(**data_dict) for data_dict in data_list]
        Department.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
