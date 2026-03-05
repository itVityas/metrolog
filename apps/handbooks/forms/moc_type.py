from django import forms
from ..models import MocType


class MocTypeForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
    type = forms.CharField(
        label='Тип СИ',
        widget=forms.TextInput(attrs={
            'placeholder': 'Тип СИ',
            'class': 'form-control'
        }),
        initial='',
        required=True,
        max_length=50
    )
    code = forms.IntegerField(
        label='Код',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Код',
            'class': 'form-control'
        }),
        initial=0,
        required=True
    )
    accurancy = forms.DecimalField(
        label='Точность',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Точность',
            'class': 'form-control'
        }),
        max_digits=10,
        decimal_places=5,
        initial=0,
        required=True
    )
    cost = forms.DecimalField(
        label='Стоимость госповерки',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Стоимость госповерки',
            'class': 'form-control'
        }),
        max_digits=9,
        decimal_places=2,
        initial=0,
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
        required=True,
        max_length=5
    )
    max_measurement = forms.CharField(
        label='Единица изм. макс. предела',
        widget=forms.TextInput(attrs={
            'placeholder': 'Единица изм. макс. предела',
            'class': 'form-control'
        }),
        initial='',
        required=True,
        max_length=5
    )
    standart_verification = forms.DecimalField(
        label='Норма поверки',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Норма поверки',
            'class': 'form-control'
        }),
        max_digits=2,
        decimal_places=1,
        initial=0,
        required=True
    )
    standart_repair = forms.DecimalField(
        label='Норма ремонта',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Норма ремонта',
            'class': 'form-control'
        }),
        max_digits=2,
        decimal_places=1,
        initial=0,
        required=True
    )
    rank_verification = forms.IntegerField(
        label='Разряд поверителя',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Разряд поверителя',
            'class': 'form-control'
        }),
        initial=0,
        required=True
    )
    rank_repair = forms.IntegerField(
        label='Разряд ремонтника',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Разряд ремонтника',
            'class': 'form-control'
        }),
        initial=0,
        required=True
    )

    class Meta:
        model = MocType
        fields = ['id', 'type', 'code', 'accurancy', 'cost',
                  'min_limit', 'max_limit', 'min_measurement',
                  'max_measurement', 'standart_verification',
                  'standart_repair', 'rank_verification', 'rank_repair']
