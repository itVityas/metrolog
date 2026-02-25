from django import forms
from ..models import Department


class DepartmentForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
    workshop = forms.IntegerField(
        label='workshop',
        widget=forms.NumberInput(attrs={
            'placeholder': 'workshop',
            'class': 'form-control'
        }),
        initial=0,
        required=True
    )
    brigade = forms.IntegerField(
        label='brigade',
        widget=forms.NumberInput(attrs={
            'placeholder': 'brigade',
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
        widget=forms.NumberInput(attrs={
            'placeholder': 'Активно',
            'class': 'form-control'
        }),
        initial=False,
        required=True
    )

    class Meta:
        model = Department
        fields = ['id', 'workshop', 'brigade', 'name', 'is_active']
