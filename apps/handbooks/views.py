from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (MocGroup,
                     ChangeType,
                     Department,
                     Repair,
                     PreciousMetals,
                     VerificationDepartment,
                     VerificationPerson,
                     RepairCode,
                     InstrumentFailure,
                     DeviceStatus,
                     MocType,
                     UnitsMeasurement,
                     MocLimit,
                     VerificationSign,
                     RepairDepartment,)
from .forms import (MocGroupForm,
                    ChangeTypeForm,
                    DepartmentForm,
                    RepairForm,
                    PreciousMetalsForm,
                    VerificationDepartmentForm,
                    VerificationPersonForm,
                    RepairCodeForm,
                    InstrumentFailureForm,
                    DeviceStatusForm,
                    MocTypeForm,
                    UnitsMeasurementForm,
                    MocLimitForm,
                    VerificationSignForm,
                    RepairDepartmentForm,)
from django.http import HttpResponseRedirect


class MocGroupListView(LoginRequiredMixin, ListView):
    """
        ListView for MocGroup
    """
    model = MocGroup
    template_name = 'handbooks/tables/moc_group_table.html'
    form = MocGroupForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class ChangeTypeListView(LoginRequiredMixin, ListView):
    """
        ListView for ChangeType
    """
    model = ChangeType
    template_name = 'handbooks/tables/change_type_table.html'
    form = ChangeTypeForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = ChangeTypeForm
        return context


class ChangeTypeAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for ChangeType
    """
    model = ChangeType
    form_class = ChangeTypeForm
    success_url = reverse_lazy('change_type')


class ChangeTypeUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for ChangeType
    """
    model = ChangeType
    form_class = ChangeTypeForm
    success_url = reverse_lazy('change_type')


class ChangeTypeDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for ChangeType
    """
    model = ChangeType
    form_class = ChangeTypeForm
    success_url = reverse_lazy('change_type')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class DepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for Department
    """
    model = Department
    template_name = 'handbooks/tables/department_table.html'
    form = DepartmentForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = DepartmentForm
        return context


class DepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for Department
    """
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department')


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for Department
    """
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department')


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for Department
    """
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('department')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class RepairListView(LoginRequiredMixin, ListView):
    """
        ListView for Repair
    """
    model = Repair
    template_name = 'handbooks/tables/repair_table.html'
    form = RepairForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = RepairForm
        return context


class RepairAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for Repair
    """
    model = Repair
    form_class = RepairForm
    success_url = reverse_lazy('repair')


class RepairUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for Repair
    """
    model = Repair
    form_class = RepairForm
    success_url = reverse_lazy('repair')


class RepairDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for Repair
    """
    model = Repair
    form_class = RepairForm
    success_url = reverse_lazy('repair')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class PreciousMetalsListView(LoginRequiredMixin, ListView):
    """
        ListView for PreciousMetals
    """
    model = PreciousMetals
    template_name = 'handbooks/tables/precious_metals_table.html'
    form = PreciousMetalsForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class VerificationDepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for VerificationDepartment
    """
    model = VerificationDepartment
    template_name = 'handbooks/tables/verification_department_table.html'
    form = VerificationDepartmentForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = VerificationDepartmentForm
        return context


class VerificationDepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for VerificationDepartment
    """
    model = VerificationDepartment
    form_class = VerificationDepartmentForm
    success_url = reverse_lazy('verification_department')


class VerificationDepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for VerificationDepartment
    """
    model = VerificationDepartment
    form_class = VerificationDepartmentForm
    success_url = reverse_lazy('verification_department')


class VerificationDepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for VerificationDepartment
    """
    model = VerificationDepartment
    form_class = VerificationDepartmentForm
    success_url = reverse_lazy('verification_department')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class VerificationPersonListView(LoginRequiredMixin, ListView):
    """
        ListView for VerificationPerson
    """
    model = VerificationPerson
    template_name = 'handbooks/tables/verification_person_table.html'
    form = VerificationPersonForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = VerificationPersonForm
        return context


class VerificationPersonAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for VerificationPerson
    """
    model = VerificationPerson
    form_class = VerificationPersonForm
    success_url = reverse_lazy('verification_person')


class VerificationPersonUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for VerificationPerson
    """
    model = VerificationPerson
    form_class = VerificationPersonForm
    success_url = reverse_lazy('verification_person')


class VerificationPersonDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for VerificationPerson
    """
    model = VerificationPerson
    form_class = VerificationPersonForm
    success_url = reverse_lazy('verification_person')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class RepairCodeListView(LoginRequiredMixin, ListView):
    """
        ListView for RepairCode
    """
    model = RepairCode
    template_name = 'handbooks/tables/repair_code_table.html'
    form = RepairCodeForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = RepairCodeForm
        return context


class RepairCodeAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for RepairCode
    """
    model = RepairCode
    form_class = RepairCodeForm
    success_url = reverse_lazy('repair_code')


class RepairCodeUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for RepairCode
    """
    model = RepairCode
    form_class = RepairCodeForm
    success_url = reverse_lazy('repair_code')


class RepairCodeDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for RepairCode
    """
    model = RepairCode
    form_class = RepairCodeForm
    success_url = reverse_lazy('repair_code')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class InstrumentFailureListView(LoginRequiredMixin, ListView):
    """
        ListView for InstrumentFailure
    """
    model = InstrumentFailure
    template_name = 'handbooks/tables/instrument_failure_table.html'
    form = InstrumentFailureForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class DeviceStatusListView(LoginRequiredMixin, ListView):
    """
        ListView for DeviceStatus
    """
    model = DeviceStatus
    template_name = 'handbooks/tables/device_status_table.html'
    form = DeviceStatusForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = DeviceStatusForm
        return context


class DeviceStatusAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for DeviceStatus
    """
    model = DeviceStatus
    form_class = DeviceStatusForm
    success_url = reverse_lazy('device_status')


class DeviceStatusUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for DeviceStatus
    """
    model = DeviceStatus
    form_class = DeviceStatusForm
    success_url = reverse_lazy('device_status')


class DeviceStatusDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for DeviceStatus
    """
    model = DeviceStatus
    form_class = DeviceStatusForm
    success_url = reverse_lazy('device_status')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class MocTypeListView(LoginRequiredMixin, ListView):
    """
        ListView for MocType
    """
    model = MocType
    template_name = 'handbooks/tables/moc_type_table.html'
    form = MocTypeForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = MocTypeForm
        return context


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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class UnitsMeasurementListView(LoginRequiredMixin, ListView):
    """
        ListView for UnitsMeasurement
    """
    model = UnitsMeasurement
    template_name = 'handbooks/tables/units_measurement_table.html'
    form = UnitsMeasurementForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = UnitsMeasurementForm
        return context


class UnitsMeasurementAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for UnitsMeasurement
    """
    model = UnitsMeasurement
    form_class = UnitsMeasurementForm
    success_url = reverse_lazy('units_measurement')


class UnitsMeasurementUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for UnitsMeasurement
    """
    model = UnitsMeasurement
    form_class = UnitsMeasurementForm
    success_url = reverse_lazy('units_measurement')


class UnitsMeasurementDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for UnitsMeasurement
    """
    model = UnitsMeasurement
    form_class = UnitsMeasurementForm
    success_url = reverse_lazy('units_measurement')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class MocLimitListView(LoginRequiredMixin, ListView):
    """
        ListView for MocLimit
    """
    model = MocLimit
    template_name = 'handbooks/tables/moc_limit_table.html'
    form = MocLimitForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class VerificationSignListView(LoginRequiredMixin, ListView):
    """
        ListView for VerificationSign
    """
    model = VerificationSign
    template_name = 'handbooks/tables/verification_sign_table.html'
    form = VerificationSignForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class RepairDepartmentListView(LoginRequiredMixin, ListView):
    """
        ListView for RepairDepartment
    """
    model = RepairDepartment
    template_name = 'handbooks/tables/repair_department_table.html'
    form = RepairDepartmentForm
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = RepairDepartmentForm
        return context


class RepairDepartmentAddView(LoginRequiredMixin, CreateView):
    """
        CreateView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')


class RepairDepartmentUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')


class RepairDepartmentDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for RepairDepartment
    """
    model = RepairDepartment
    form_class = RepairDepartmentForm
    success_url = reverse_lazy('repair_department')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
