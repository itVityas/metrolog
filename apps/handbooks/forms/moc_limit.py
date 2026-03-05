from django import forms
from ..models import MocLimit


class MocLimitForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
    type = forms.CharField(
        label='Тип',
        widget=forms.TextInput(attrs={
            'placeholder': 'Тип',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )
    min_limit = forms.DecimalField(
        label='Мин. предел измерения',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Мин. предел измерения',
            'class': 'form-control'
        }),
        max_digits=10,
        decimal_places=5,
        initial=0,
        required=True
    )
    max_limit = forms.DecimalField(
        label='Макс. предел измерения',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Макс. предел измерения',
            'class': 'form-control'
        }),
        max_digits=10,
        decimal_places=5,
        initial=0,
        required=True
    )
    min_measurement = forms.CharField(
        label='Единица изм. мин. предела',
        widget=forms.TextInput(attrs={
            'placeholder': 'Единица изм. мин. предела',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )
    max_measurement = forms.CharField(
        label='Единица изм. макс. предела',
        widget=forms.TextInput(attrs={
            'placeholder': 'Единица изм. макс. предела',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )

    class Meta:
        model = MocLimit
        fields = ['id', 'type', 'min_limit', 'max_limit',
                  'min_measurement', 'max_measurement']
