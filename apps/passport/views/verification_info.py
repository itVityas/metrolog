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


class VerificationInfoCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for VerificationInfo
    """
    model = models.VerificationInfo
    form_class = forms.VerificationInfoForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class VerificationInfoUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for VerificationInfo
    """
    model = models.VerificationInfo
    form_class = forms.VerificationInfoForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class VerificationInfoDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for VerificationInfo
    """
    model = models.VerificationInfo
    form_class = forms.VerificationInfoForm
    success_url = reverse_lazy('passport')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        response.status_code = 303
        return response


class PassportVerificationPersonView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new VerificationPerson
    """
    model = h_models.VerificationPerson
    form_class = h_forms.VerificationPersonForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.VerificationInfoForm()
        return render(request,
                      'passport/modals/moc_list_table_modal.html',
                      {'tform': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.VerificationPersonForm()
        return render(request,
                      'handbooks/modals/passport_table_modal.html',
                      {'form': form,
                       'modal_name': 'verification',
                       'field_name': 'verification_person'})


class PassportVerificationSignView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new VerificationSign
    """
    model = h_models.VerificationSign
    form_class = h_forms.VerificationSignForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.VerificationInfoForm()
        return render(request,
                      'passport/modals/moc_list_table_modal.html',
                      {'tform': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.VerificationSignForm()
        return render(request,
                      'handbooks/modals/passport_table_modal.html',
                      {'form': form,
                       'modal_name': 'verification',
                       'field_name': 'verification_sign'})
