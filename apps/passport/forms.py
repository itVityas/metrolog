from django import forms
from . import models
from ..handbooks import models as hmodels
from django.forms import ModelChoiceField
import datetime


class MocListForm(forms.ModelForm):

    class MocGroupChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    class MocTypeChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.type

    class ChangeTypeChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    class VerificationDepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    moc_group = MocGroupChoiceField(
        hmodels.MocGroup.objects.all(),
        label='Наименование прибора'
    )

    moc_type = MocTypeChoiceField(
        hmodels.MocType.objects.all(),
        label='Тип'
    )

    change_type = ChangeTypeChoiceField(
        hmodels.ChangeType.objects.all(),
        label='Вид измерения'
    )

    verification_department = ChangeTypeChoiceField(
        hmodels.VerificationDepartment.objects.all(),
        label='Поверочное подразделение'
    )

    class Meta:
        model = models.MocList
        fields = ("__all__")


class MocMetalsForm(forms.ModelForm):

    class PreciousMetalsChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    class MocListChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.id

    precious_metals = PreciousMetalsChoiceField(
        hmodels.PreciousMetals.objects.all(),
        label='Драгметалл'
    )

    moc_list = MocListChoiceField(
        models.MocList.objects.all(),
        label='moc_list',
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = models.MocMetals
        fields = ("__all__")


class VerificationInfoForm(forms.ModelForm):

    class VerificationPersonChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.fio

    class VerificationSignChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    class MocListChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.id

    verification_person = VerificationPersonChoiceField(
        hmodels.VerificationPerson.objects.all(),
        label='Поверитель'
    )

    verification_sign = VerificationSignChoiceField(
        hmodels.VerificationSign.objects.all(),
        label='Признак поверки'
    )

    moc_list = MocListChoiceField(
        models.MocList.objects.all(),
        label='moc_list',
        widget=forms.HiddenInput(),
    )

    inv_number = forms.CharField(
        widget=forms.TextInput(),
        label='Инвентарный номер',
        max_length=20,
    )

    entry_date = forms.DateField(
        label='Дата поступления на поверку',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    verification_date = forms.DateField(
        label='Дата поверки',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    workshop_issue_date = forms.DateField(
        label='Дата выдачи в цех',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    class Meta:
        model = models.VerificationInfo
        fields = ("__all__")


class RepairInfoForm(forms.ModelForm):

    class RepairChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    class RepairCodeChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    class VerificationSignChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    class RepairDepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    class MocListChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.id

    entry_date = forms.DateField(
        label='Дата выдачи',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    entry_repair_date = forms.DateField(
        label='Дата выдачи в ремонт',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    repair_date = forms.DateField(
        label='Дата ремонта',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    moc_list = MocListChoiceField(
        models.MocList.objects.all(),
        label='moc_list',
        widget=forms.HiddenInput(),
    )

    repair = RepairChoiceField(
        hmodels.Repair.objects.all(),
        label='Хар-р ремонта',
    )

    repair_code = RepairCodeChoiceField(
        hmodels.RepairCode.objects.all(),
        label='Кат. ремонта',
    )

    repair_department = RepairDepartmentChoiceField(
        hmodels.RepairDepartment.objects.all(),
        label='Ремонтник',
    )

    verification_sign = VerificationSignChoiceField(
        hmodels.VerificationSign.objects.all(),
        label='Причина отказа',
    )

    class Meta:
        model = models.RepairInfo
        fields = ("__all__")


class DeviceLocationForm(forms.ModelForm):

    class DepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return f"{obj.workshop} - {obj.brigade}"

    class MocListChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.id

    entry_date = forms.DateField(
        label='Дата выдачи',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    moc_list = MocListChoiceField(
        models.MocList.objects.all(),
        label='moc_list',
        widget=forms.HiddenInput(),
    )

    department = DepartmentChoiceField(
        hmodels.Department.objects.all().order_by('workshop'),
        label='Цех - Бригада',
    )

    class Meta:
        model = models.DeviceLocation
        fields = ("__all__")


class DeviceStatusDateForm(forms.ModelForm):

    class DeviceStatusChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return f"{obj.name}"

    class MocListChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.id

    status_date = forms.DateField(
        label='Дата присвоения',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    moc_list = MocListChoiceField(
        models.MocList.objects.all(),
        label='moc_list',
        widget=forms.HiddenInput(),
    )

    device_status = DeviceStatusChoiceField(
        hmodels.DeviceStatus.objects.all(),
        label='Статус',
    )

    class Meta:
        model = models.DeviceStatusDate
        fields = ("__all__")


class DeviceStationForm(forms.ModelForm):

    class Meta:
        model = models.DeviceStation
        fields = ("__all__")
