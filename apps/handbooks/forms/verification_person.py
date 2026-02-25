from django import forms
from ..models import VerificationPerson


class VerificationPersonForm(forms.ModelForm):
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
    rank = forms.IntegerField(
        label='Разряд',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Разряд',
            'class': 'form-control'
        }),
        initial=0,
        required=True
    )
    fio = forms.CharField(
        label='Фио',
        widget=forms.TextInput(attrs={
            'placeholder': 'Фио',
            'class': 'form-control'
        }),
        initial='',
        required=True
    )
    is_active = forms.BooleanField(
        label='Активен',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Активен',
            'class': 'form-control'
        }),
        initial=False,
        required=True
    )

    class Meta:
        model = VerificationPerson
        fields = ['id', 'code', 'rank', 'fio', 'is_active']
