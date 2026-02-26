from django import forms
from ..models import VerificationDepartment


class VerificationDepartmentForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
    code = forms.IntegerField(
        label='Код',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Код',
            'class': 'form-control'
        }),
        initial=0,
        required=True
    )
    sign = forms.IntegerField(
        label='Признак',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Признак',
            'class': 'form-control'
        }),
        initial=0,
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
    is_active = forms.BooleanField(
        label='Активно',
        widget=forms.CheckboxInput(attrs={
            'placeholder': 'Активно',
        }),
        initial=False,
        required=False
    )

    class Meta:
        model = VerificationDepartment
        fields = ['id', 'code', 'sign', 'name', 'is_active']
