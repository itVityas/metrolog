from django import forms
from . import models
from ..handbooks import models as hmodels
from django.forms import ModelChoiceField


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

    class Meta:
        model = models.MocMetals
        fields = ("__all__")


class VerificationInfoForm(forms.ModelForm):

    class Meta:
        model = models.VerificationInfo
        fields = ("__all__")


class RepairInfoForm(forms.ModelForm):

    class Meta:
        model = models.RepairInfo
        fields = ("__all__")


class DeviceLocationForm(forms.ModelForm):

    class Meta:
        model = models.DeviceLocation
        fields = ("__all__")


class DeviceStatusDateForm(forms.ModelForm):

    class Meta:
        model = models.DeviceStatusDate
        fields = ("__all__")


class DeviceStationForm(forms.ModelForm):

    class Meta:
        model = models.DeviceStation
        fields = ("__all__")
