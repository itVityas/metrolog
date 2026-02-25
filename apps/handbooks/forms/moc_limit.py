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
        label='Мин. лимит',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Мин. лимит',
            'class': 'form-control'
        }),
        max_digits=10,
        decimal_places=5,
        initial=0,
        required=True
    )
    max_limit = forms.DecimalField(
        label='Макс. лимит',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Макс. лимит',
            'class': 'form-control'
        }),
        max_digits=10,
        decimal_places=5,
        initial=0,
        required=True
    )
    min_measurement = forms.CharField(
        label='Мин. измерение',
        widget=forms.TextInput(attrs={
            'placeholder': 'Мин. измерение',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )
    max_measurement = forms.CharField(
        label='Макс. измерение',
        widget=forms.TextInput(attrs={
            'placeholder': 'Макс. измерение',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )

    class Meta:
        model = MocLimit
        fields = ['id', 'type', 'min_limit', 'max_limit',
                  'min_measurement', 'max_measurement']
