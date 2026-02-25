from django import forms
from ..models import UnitsMeasurement


class UnitsMeasurementForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
    code = forms.CharField(
        label='Код',
        widget=forms.TextInput(attrs={
            'placeholder': 'Код',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )
    name = forms.CharField(
        label='Название',
        widget=forms.TextInput(attrs={
            'placeholder': 'Название',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )

    class Meta:
        model = UnitsMeasurement
        fields = ['id', 'code', 'name']
