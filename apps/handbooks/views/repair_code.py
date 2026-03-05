from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import RepairCode
from ..forms import RepairCodeForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class RepairCodeListView(LoginRequiredMixin, ListView):
    """
        ListView for RepairCode
    """
    model = RepairCode
    template_name = 'handbooks/tables/repair_code_table.html'
    form = RepairCodeForm
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
        context['form'] = RepairCodeForm
        return context


class RepairCodeAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for RepairCode
    """
    model = RepairCode
    form_class = RepairCodeForm
    success_url = reverse_lazy('repair_code')


class RepairCodeUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for RepairCode
    """
    model = RepairCode
    form_class = RepairCodeForm
    success_url = reverse_lazy('repair_code')


class RepairCodeDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for RepairCode
    """
    model = RepairCode
    form_class = RepairCodeForm
    success_url = reverse_lazy('repair_code')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class RepairCodeMigrateView(LoginRequiredMixin, View):
    model = RepairCode
    success_url = reverse_lazy('repair_code')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb014.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['code'] = record.get('KAT_REM')
            new_dict['name'] = record.get('NAME_REM')
            data_list.append(new_dict)

        obj_list = [RepairCode(**data_dict) for data_dict in data_list]
        RepairCode.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
