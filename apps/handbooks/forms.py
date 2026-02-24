from django import forms
from .models import (MocGroup,
                     ChangeType,
                     Department,
                     Repair,
                     PreciousMetals,
                     VerificationDepartment,
                     VerificationPerson,
                     RepairCode,
                     InstrumentFailure,
                     DeviceStatus,
                     MocType,
                     UnitsMeasurement,
                     MocLimit,
                     VerificationSign,
                     RepairDepartment,)


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


class ChangeTypeForm(forms.ModelForm):
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
        model = ChangeType
        fields = ['id', 'code', 'name']


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


class RepairForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
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
        model = Repair
        fields = ['id', 'name']


class PreciousMetalsForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
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
        model = PreciousMetals
        fields = ['id', 'name']


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
        label='Знак',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Знак',
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
        model = VerificationDepartment
        fields = ['id', 'code', 'sign', 'name', 'is_active']


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


class RepairCodeForm(forms.ModelForm):
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
        model = RepairCode
        fields = ['id', 'code', 'name']


class InstrumentFailureForm(forms.ModelForm):
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
        model = InstrumentFailure
        fields = ['id', 'code', 'name']


class DeviceStatusForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(),
                         initial='', required=False)
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
        model = DeviceStatus
        fields = ['id', 'name']


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
                  'min_limt', 'max_limit', 'min_measurement',
                  'max_measurement', 'standart_verification',
                  'standart_repair', 'rank_verification', 'rank_repair']


class UnitsMeasurementForm(forms.ModelForm):
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
        model = UnitsMeasurement
        fields = ['id', 'code', 'name']


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


class VerificationSignForm(forms.ModelForm):
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
        model = VerificationSign
        fields = ['id', 'code', 'name']


class RepairDepartmentForm(forms.ModelForm):
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
        label='Знак',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Знак',
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
        widget=forms.NumberInput(attrs={
            'placeholder': 'Активен',
            'class': 'form-control'
        }),
        initial=False,
        required=True
    )

    class Meta:
        model = RepairDepartment
        fields = ['id', 'code', 'sign', 'name', 'is_active']
