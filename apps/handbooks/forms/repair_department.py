from django import forms
from ..models import RepairDepartment


class RepairDepartmentForm(forms.ModelForm):
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
    sign = forms.IntegerField(
        label='Разряд',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Разряд',
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
        label='Активен',
        widget=forms.CheckboxInput(attrs={
            'placeholder': 'Активно',
        }),
        initial=False,
        required=False
    )

    class Meta:
        model = RepairDepartment
        fields = ['id', 'code', 'sign', 'name', 'is_active']
