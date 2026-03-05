from django import forms
from ..models import ChangeType


class ChangeTypeForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
    code = forms.CharField(
        label='Код вида измерения',
        widget=forms.TextInput(attrs={
            'placeholder': 'Код вида измерения',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )
    name = forms.CharField(
        label='Наименование',
        widget=forms.TextInput(attrs={
            'placeholder': 'Наименование',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )

    class Meta:
        model = ChangeType
        fields = ['id', 'code', 'name']
