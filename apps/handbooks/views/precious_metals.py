from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import PreciousMetals
from ..forms import PreciousMetalsForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class PreciousMetalsListView(LoginRequiredMixin, ListView):
    """
        ListView for PreciousMetals
    """
    model = PreciousMetals
    template_name = 'handbooks/tables/precious_metals_table.html'
    form = PreciousMetalsForm
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
        context['form'] = PreciousMetalsForm
        return context


class PreciousMetalsAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for PreciousMetals
    """
    model = PreciousMetals
    form_class = PreciousMetalsForm
    success_url = reverse_lazy('precious_metals')


class PreciousMetalsUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for PreciousMetals
    """
    model = PreciousMetals
    form_class = PreciousMetalsForm
    success_url = reverse_lazy('precious_metals')


class PreciousMetalsDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for PreciousMetals
    """
    model = PreciousMetals
    form_class = PreciousMetalsForm
    success_url = reverse_lazy('precious_metals')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class PreciousMetalsMigrateView(LoginRequiredMixin, View):
    model = PreciousMetals
    success_url = reverse_lazy('precious_metals')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb006.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['name'] = record.get('NKM')
            data_list.append(new_dict)

        obj_list = [PreciousMetals(**data_dict) for data_dict in data_list]
        PreciousMetals.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
