from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  View)
from django.contrib.auth.mixins import LoginRequiredMixin
from .. import models
from .. import forms
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.conf import settings
from dbfread import DBF


class PassportListView(LoginRequiredMixin, ListView):
    """
        Passport List View
    """
    template_name = 'passport/moc_list.html'
    model = models.MocList
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = 'id'

    def get_queryset(self):
        queryset = models.MocList.objects.prefetch_related(
            'device_location',
            'verification_info',
            'repair_info',
            'device_status_date',
            'moc_metals').all().order_by('id')
        query = self.request.GET.get('q')

        if query:
            # Filter the queryset
            queryset = queryset.filter(
                Q(moc_group__name__icontains=query) |
                Q(moc_type__type__icontains=query)
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.MocListForm
        return context


class MocListDetailView(LoginRequiredMixin, DetailView):
    """
        DetailView for MocList
    """
    template_name = 'passport/passport_main.html'
    model = models.MocList
    form_class = forms.MocListForm
    success_url = reverse_lazy('passport')

    def get_queryset(self):
        queryset = models.MocList.objects.prefetch_related(
            'device_location',
            'verification_info',
            'repair_info',
            'device_status_date',
            'moc_metals').all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.MocListForm
        context['table_forms'] = {'verification': forms.VerificationInfoForm,
                                  'repair': forms.RepairInfoForm,
                                  'location': forms.DeviceLocationForm,
                                  'status': forms.DeviceStatusDateForm,
                                  'metall': forms.MocMetalsForm}
        return context


class MocListCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for MocList
    """
    model = models.MocList
    form_class = forms.MocListForm
    success_url = reverse_lazy('passport')


class MocListUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for MocList
    """
    model = models.MocList
    form_class = forms.MocListForm
    success_url = reverse_lazy('passport')


class MocListDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for MocList
    """
    model = models.MocList
    form_class = forms.MocListForm
    success_url = reverse_lazy('passport')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response
