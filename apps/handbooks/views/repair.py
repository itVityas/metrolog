from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Repair
from ..forms import RepairForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class RepairListView(LoginRequiredMixin, ListView):
    """
        ListView for Repair
    """
    model = Repair
    template_name = 'handbooks/tables/repair_table.html'
    form = RepairForm
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
        context['form'] = RepairForm
        return context


class RepairAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for Repair
    """
    model = Repair
    form_class = RepairForm
    success_url = reverse_lazy('repair')


class RepairUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for Repair
    """
    model = Repair
    form_class = RepairForm
    success_url = reverse_lazy('repair')


class RepairDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for Repair
    """
    model = Repair
    form_class = RepairForm
    success_url = reverse_lazy('repair')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class RepairMigrateView(LoginRequiredMixin, View):
    model = Repair
    success_url = reverse_lazy('repair')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb005.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['name'] = record.get('NREM')
            if new_dict['name'] is None:
                continue
            else:
                data_list.append(new_dict)

        obj_list = [Repair(**data_dict) for data_dict in data_list]
        Repair.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
