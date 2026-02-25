from django import forms
from ..models import MocGroup


class MocGroupForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
    type = forms.IntegerField(
        label='Тип',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Тип',
            'class': 'form-control'
        }),
        initial=0,
        required=True
    )
    group = forms.IntegerField(
        label='Группа',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Группа',
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

    class Meta:
        model = MocGroup
        fields = ['id', 'type', 'group', 'name']
