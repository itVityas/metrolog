from django import forms
from ..models import MocType


class MocTypeForm(forms.ModelForm):
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
        decimal_places=10,
        initial=0,
        required=True
    )
    cost = forms.DecimalField(
        label='Цена',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Цена',
            'class': 'form-control'
        }),
        max_digits=9,
        decimal_places=2,
        initial=0,
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
    standart_verification = forms.DecimalField(
        label='Стандарт поверки',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Стандарт поверки',
            'class': 'form-control'
        }),
        max_digits=2,
        decimal_places=1,
        initial=0,
        required=True
    )
    standart_repair = forms.DecimalField(
        label='Стандартный ремонт',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Стандартный ремонт',
            'class': 'form-control'
        }),
        max_digits=2,
        decimal_places=1,
        initial=0,
        required=True
    )
    rank_verification = forms.IntegerField(
        label='Разряд поверки',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Разряд поверки',
            'class': 'form-control'
        }),
        initial=0,
        required=True
    )
    rank_repair = forms.IntegerField(
        label='Разряд ремонта',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Разряд ремонта',
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
