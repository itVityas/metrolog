from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import MocType
from ..forms import MocTypeForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings
from django.db.models import Q


class MocTypeListView(LoginRequiredMixin, ListView):
    """
        ListView for MocType
    """
    model = MocType
    template_name = 'handbooks/tables/moc_type_table.html'
    form = MocTypeForm
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = 'id'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'id')
        return ordering

    def get_paginate_by(self, queryset):
        if 'no_page' in self.request.GET:
            return None
        user_settings = self.request.user.usersettings
        pagination_size = user_settings.pagination_size
        return pagination_size if pagination_size else self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # paginaton, deal wih too many pages
        page = context['page_obj']
        if page:
            context['paginator_range'] = page.paginator.get_elided_page_range(
                page.number, on_each_side=2, on_ends=1
            )
        # verbose names in template
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = MocTypeForm
        context['ordering'] = self.get_ordering()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            # Filter the queryset
            queryset = queryset.filter(
                Q(id__icontains=query) |
                Q(type__icontains=query) |
                Q(code__icontains=query) |
                Q(accurancy__icontains=query) |
                Q(min_limit__icontains=query) |
                Q(max_limit__icontains=query) |
                Q(min_measurement__icontains=query) |
                Q(max_measurement__icontains=query) |
                Q(standart_verification__icontains=query) |
                Q(standart_repair__icontains=query) |
                Q(rank_verification__icontains=query) |
                Q(rank_repair__icontains=query)
            ).distinct()
        return queryset


class MocTypeAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for MocType
    """
    model = MocType
    form_class = MocTypeForm
    success_url = reverse_lazy('moc_type')


class MocTypeUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for MocType
    """
    model = MocType
    form_class = MocTypeForm
    success_url = reverse_lazy('moc_type')


class MocTypeDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for MocType
    """
    model = MocType
    form_class = MocTypeForm
    success_url = reverse_lazy('moc_type')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class MocTypeMigrateView(LoginRequiredMixin, View):
    model = MocType
    success_url = reverse_lazy('moc_type')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb008.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['type'] = record.get('TIP_SI')
            new_dict['code'] = record.get('KOD_SI')
            new_dict['accurancy'] = record.get('TOCH')
            new_dict['cost'] = record.get('ST_G_P')
            new_dict['min_limit'] = record.get('MIN_PRED')
            new_dict['max_limit'] = record.get('MAX_PRED')
            new_dict['min_measurement'] = record.get('ED_IZ_MIN')
            new_dict['max_measurement'] = record.get('ED_IZ_MAX')
            new_dict['standart_verification'] = record.get('NORM_POV')
            new_dict['standart_repair'] = record.get('NORM_REM')
            new_dict['rank_verification'] = record.get('RAZR_POV')
            new_dict['rank_repair'] = record.get('RAZR_REM')
            data_list.append(new_dict)

        obj_list = [MocType(**data_dict) for data_dict in data_list]
        MocType.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
