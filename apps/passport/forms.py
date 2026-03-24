from django import forms
from . import models


class MocListForm(forms.ModelForm):

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
