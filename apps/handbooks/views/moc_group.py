from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import MocGroup
from ..forms import MocGroupForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class MocGroupListView(LoginRequiredMixin, ListView):
    """
        ListView for MocGroup
    """
    model = MocGroup
    template_name = 'handbooks/tables/moc_group_table.html'
    form = MocGroupForm
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
        context['form'] = MocGroupForm
        return context


class MocGroupAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for MocGroup
    """
    model = MocGroup
    form_class = MocGroupForm
    success_url = reverse_lazy('moc_group')


class MocGroupUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for MocGroup
    """
    model = MocGroup
    form_class = MocGroupForm
    success_url = reverse_lazy('moc_group')


class MocGroupDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for MocGroup
    """
    model = MocGroup
    form_class = MocGroupForm
    success_url = reverse_lazy('moc_group')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class MocGroupMigrateView(LoginRequiredMixin, View):
    model = MocGroup
    success_url = reverse_lazy('moc_group')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb001.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['type'] = record.get('VID_IZ')
            new_dict['group'] = record.get('GR_SI')
            new_dict['name'] = record.get('NGR_SI')
            data_list.append(new_dict)

        obj_list = [MocGroup(**data_dict) for data_dict in data_list]
        MocGroup.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
