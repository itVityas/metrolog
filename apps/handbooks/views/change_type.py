from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import ChangeType
from ..forms import ChangeTypeForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class ChangeTypeListView(LoginRequiredMixin, ListView):
    """
        ListView for ChangeType
    """
    model = ChangeType
    template_name = 'handbooks/tables/change_type_table.html'
    form = ChangeTypeForm
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
        context['form'] = ChangeTypeForm
        return context


class ChangeTypeAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for ChangeType
    """
    model = ChangeType
    form_class = ChangeTypeForm
    success_url = reverse_lazy('change_type')


class ChangeTypeUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for ChangeType
    """
    model = ChangeType
    form_class = ChangeTypeForm
    success_url = reverse_lazy('change_type')


class ChangeTypeDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for ChangeType
    """
    model = ChangeType
    form_class = ChangeTypeForm
    success_url = reverse_lazy('change_type')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class ChangeTypeMigrateView(LoginRequiredMixin, View):
    model = ChangeType
    success_url = reverse_lazy('change_type')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb004.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['code'] = record.get('VID_IZ')
            new_dict['name'] = record.get('NVID_IZ')
            data_list.append(new_dict)

        obj_list = [ChangeType(**data_dict) for data_dict in data_list]
        ChangeType.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
