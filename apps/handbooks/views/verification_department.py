from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import VerificationDepartment
from ..forms import VerificationDepartmentForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class VerificationDepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for VerificationDepartment
    """
    model = VerificationDepartment
    template_name = 'handbooks/tables/verification_department_table.html'
    form = VerificationDepartmentForm
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
        context['form'] = VerificationDepartmentForm
        return context


class VerificationDepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for VerificationDepartment
    """
    model = VerificationDepartment
    form_class = VerificationDepartmentForm
    success_url = reverse_lazy('verification_department')


class VerificationDepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for VerificationDepartment
    """
    model = VerificationDepartment
    form_class = VerificationDepartmentForm
    success_url = reverse_lazy('verification_department')


class VerificationDepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for VerificationDepartment
    """
    model = VerificationDepartment
    form_class = VerificationDepartmentForm
    success_url = reverse_lazy('verification_department')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class VerificationDepartmentMigrateView(LoginRequiredMixin, View):
    model = VerificationDepartment
    success_url = reverse_lazy('verification_department')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb010.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['code'] = record.get('KOD_POD')
            new_dict['sign'] = record.get('PR')
            new_dict['name'] = record.get('NAME_POD')
            new_dict['is_active'] = True
            data_list.append(new_dict)

        obj_list = [
            VerificationDepartment(**data_dict) for data_dict in data_list]
        VerificationDepartment.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
