from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import InstrumentFailure
from ..forms import InstrumentFailureForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class InstrumentFailureListView(LoginRequiredMixin, ListView):
    """
        ListView for InstrumentFailure
    """
    model = InstrumentFailure
    template_name = 'handbooks/tables/instrument_failure_table.html'
    form = InstrumentFailureForm
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
        context['form'] = InstrumentFailureForm
        return context


class InstrumentFailureAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for InstrumentFailure
    """
    model = InstrumentFailure
    form_class = InstrumentFailureForm
    success_url = reverse_lazy('instrument_failure')


class InstrumentFailureUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for InstrumentFailure
    """
    model = InstrumentFailure
    form_class = InstrumentFailureForm
    success_url = reverse_lazy('instrument_failure')


class InstrumentFailureDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for InstrumentFailure
    """
    model = InstrumentFailure
    form_class = InstrumentFailureForm
    success_url = reverse_lazy('instrument_failure')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class InstrumentFailureMigrateView(LoginRequiredMixin, View):
    model = InstrumentFailure
    success_url = reverse_lazy('instrument_failure')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb015.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['code'] = record.get('KOD_OTK')
            new_dict['name'] = record.get('NAME_OTK')
            data_list.append(new_dict)

        obj_list = [InstrumentFailure(**data_dict) for data_dict in data_list]
        InstrumentFailure.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
