from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .. import models
from .. import forms
from django.http import HttpResponseRedirect
from apps.handbooks import forms as h_forms
from apps.handbooks import models as h_models
from django.shortcuts import render
from django.views.generic.edit import BaseFormView


class RepairInfoCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for RepairInfo
    """
    model = models.RepairInfo
    form_class = forms.RepairInfoForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class RepairInfoUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for RepairInfo
    """
    model = models.RepairInfo
    form_class = forms.RepairInfoForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class RepairInfoDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for RepairInfo
    """
    model = models.RepairInfo
    form_class = forms.RepairInfoForm
    success_url = reverse_lazy('passport')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        response.status_code = 303
        return response


class PassportRepairView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new Repair
    """
    model = h_models.Repair
    form_class = h_forms.RepairForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.RepairInfoForm()
        return render(request,
                      'passport/modals/moc_list_table_modal.html',
                      {'tform': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.RepairForm()
        return render(request,
                      'handbooks/modals/passport_table_modal.html',
                      {'form': form,
                       'modal_name': 'repair',
                       'field_name': 'repair'})


class PassportRepairCodeView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new RepairCode
    """
    model = h_models.RepairCode
    form_class = h_forms.RepairCodeForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.RepairInfoForm()
        return render(request,
                      'passport/modals/moc_list_table_modal.html',
                      {'tform': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.RepairCodeForm()
        return render(request,
                      'handbooks/modals/passport_table_modal.html',
                      {'form': form,
                       'modal_name': 'repair',
                       'field_name': 'repair_code'})


class PassportRepairDepartmentView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new RepairDepartment
    """
    model = h_models.RepairDepartment
    form_class = h_forms.RepairDepartmentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.RepairInfoForm()
        return render(request,
                      'passport/modals/moc_list_table_modal.html',
                      {'tform': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.RepairDepartmentForm()
        return render(request,
                      'handbooks/modals/passport_table_modal.html',
                      {'form': form,
                       'modal_name': 'repair',
                       'field_name': 'repair_department'})


class PassportInstrumentFailureView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new InstrumentFailure
    """
    model = h_models.InstrumentFailure
    form_class = h_forms.InstrumentFailureForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.RepairInfoForm()
        return render(request,
                      'passport/modals/moc_list_table_modal.html',
                      {'tform': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.InstrumentFailureForm()
        return render(request,
                      'handbooks/modals/passport_table_modal.html',
                      {'form': form,
                       'modal_name': 'repair',
                       'field_name': 'instrument_failure'})
