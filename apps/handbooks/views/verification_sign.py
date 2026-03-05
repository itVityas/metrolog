from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import VerificationSign
from ..forms import VerificationSignForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings


class VerificationSignListView(LoginRequiredMixin, ListView):
    """
        ListView for VerificationSign
    """
    model = VerificationSign
    template_name = 'handbooks/tables/verification_sign_table.html'
    form = VerificationSignForm
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
        context['form'] = VerificationSignForm
        return context


class VerificationSignAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for VerificationSign
    """
    model = VerificationSign
    form_class = VerificationSignForm
    success_url = reverse_lazy('verification_sign')


class VerificationSignUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for VerificationSign
    """
    model = VerificationSign
    form_class = VerificationSignForm
    success_url = reverse_lazy('verification_sign')


class VerificationSignDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for VerificationSign
    """
    model = VerificationSign
    form_class = VerificationSignForm
    success_url = reverse_lazy('verification_sign')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class VerificationSignMigrateView(LoginRequiredMixin, View):
    model = VerificationSign
    success_url = reverse_lazy('verification_sign')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb017.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['code'] = record.get('KOD_PR')
            new_dict['name'] = record.get('NAME_PR')
            data_list.append(new_dict)

        obj_list = [VerificationSign(**data_dict) for data_dict in data_list]
        VerificationSign.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
