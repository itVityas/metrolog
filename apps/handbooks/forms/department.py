from django import forms
from ..models import Department


class DepartmentForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
    workshop = forms.IntegerField(
        label='Цех',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Цех',
            'class': 'form-control'
        }),
        initial=0,
        required=True
    )
    brigade = forms.IntegerField(
        label='Бригада',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Бригада',
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
        model = Department
        fields = ['id', 'workshop', 'brigade', 'name', 'is_active']
