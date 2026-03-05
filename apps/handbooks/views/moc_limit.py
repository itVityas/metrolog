from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import MocLimit
from ..forms import MocLimitForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class MocLimitListView(LoginRequiredMixin, ListView):
    """
        ListView for MocLimit
    """
    model = MocLimit
    template_name = 'handbooks/tables/moc_limit_table.html'
    form = MocLimitForm
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
        context['form'] = MocLimitForm
        return context


class MocLimitAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for MocLimit
    """
    model = MocLimit
    form_class = MocLimitForm
    success_url = reverse_lazy('moc_limit')


class MocLimitUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for MocLimit
    """
    model = MocLimit
    form_class = MocLimitForm
    success_url = reverse_lazy('moc_limit')


class MocLimitDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for MocLimit
    """
    model = MocLimit
    form_class = MocLimitForm
    success_url = reverse_lazy('moc_limit')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class MocLimitMigrateView(LoginRequiredMixin, View):
    model = MocLimit
    success_url = reverse_lazy('moc_limit')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb012.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['type'] = record.get('TIP_SI')
            new_dict['min_limit'] = record.get('MIN_PRED')
            new_dict['max_limit'] = record.get('MAX_PRED')
            new_dict['min_measurement'] = record.get('ED_IZ_MIN')
            new_dict['max_measurement'] = record.get('ED_IZ_MAX')
            data_list.append(new_dict)

        obj_list = [MocLimit(**data_dict) for data_dict in data_list]
        MocLimit.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
