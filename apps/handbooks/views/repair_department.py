from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import RepairDepartment
from ..forms import RepairDepartmentForm
from django.http import HttpResponseRedirect
from django.views import View
from dbfread import DBF
from django.conf import settings
from django.db.models import Q
from django.shortcuts import redirect
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


class RepairDepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for RepairDepartment
    """
    model = RepairDepartment
    template_name = 'handbooks/tables/repair_department_table.html'
    form = RepairDepartmentForm
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
        context['form'] = RepairDepartmentForm
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            # Filter the queryset
            queryset = queryset.filter(
                Q(id__icontains=query) |
                Q(code__icontains=query) |
                Q(sign__icontains=query) |
                Q(name__icontains=query)
            ).distinct()
        return queryset


class RepairDepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        raw_url = request.META.get('HTTP_REFERER', '/')

        url_parts = list(urlparse(raw_url))
        query_params = parse_qs(url_parts[4])
        query_params['page'] = 1
        query_params['ordering'] = '-id'
        url_parts[4] = urlencode(query_params, doseq=True)
        final_url = urlunparse(url_parts)

        return redirect(final_url)


class RepairDepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        return redirect(back_url)


class RepairDepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        response.status_code = 303
        return response


class RepairDepartmentMigrateView(LoginRequiredMixin, View):
    model = RepairDepartment
    success_url = reverse_lazy('repair_department')

    def post(self, request, *args, **kwargs):
        table = DBF('dbf/mb016.DBF')

        data_list = []
        for record in table:
            new_dict = {}
            new_dict['code'] = record.get('KOD_REM')
            new_dict['sign'] = record.get('RAZR')
            new_dict['name'] = record.get('FIO')
            new_dict['is_active'] = True
            data_list.append(new_dict)

        obj_list = [RepairDepartment(**data_dict) for data_dict in data_list]
        RepairDepartment.objects.bulk_create(obj_list)
        return HttpResponseRedirect(self.success_url)
