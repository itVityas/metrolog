from django import forms
from ..handbooks import models as hmodels
from django.forms import ModelChoiceField
import datetime


class MocPresenceForm(forms.Form):

    change_type = forms.MultipleChoiceField(
        label='Вид измерения',
        widget=forms.CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['change_type'].choices = [
            (str(obj.id), obj.name) for obj in hmodels.ChangeType.objects.all().order_by('code')
        ]

    class DepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    department = DepartmentChoiceField(
        hmodels.Department.objects.all().order_by('workshop'),
        label='Подразделение'
    )


class VerificationLogForm(forms.Form):

    change_type = forms.MultipleChoiceField(
        label='Вид измерения',
        widget=forms.CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['change_type'].choices = [
            (str(obj.id), obj.name) for obj in hmodels.ChangeType.objects.all().order_by('code')
        ]

    start_date = forms.DateField(
        label='Дата начала месяца',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )


class ReceiptForm(forms.Form):

    class DepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    department = DepartmentChoiceField(
        hmodels.Department.objects.all().order_by('workshop'),
        label='Подразделение'
    )


class MocIndicatorsForm(forms.Form):

    class DepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    department = DepartmentChoiceField(
        hmodels.Department.objects.all().order_by('workshop'),
        label='Подразделение'
    )


class CompletedWorksForm(forms.Form):

    class DepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    department = DepartmentChoiceField(
        hmodels.Department.objects.all().order_by('workshop'),
        label='Подразделение'
    )

    start_date = forms.DateField(
        label='Дата начала месяца',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )


class OperatingTimeForm(forms.Form):

    start_date = forms.DateField(
        label='Дата начала периода',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )


class RepairOperatingTimeForm(forms.Form):

    start_date = forms.DateField(
        label='Дата начала месяца',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    class RepairDepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    person = RepairDepartmentChoiceField(
        hmodels.RepairDepartment.objects.all().order_by('code'),
        label='Ремонтник'
    )

    for_all = forms.BooleanField(
        required=False,
        label="Вывести для всех"
    )


class VerificationOperatingTimeForm(forms.Form):

    start_date = forms.DateField(
        label='Дата начала месяца',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    class VerificationPersonChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.fio

    person = VerificationPersonChoiceField(
        hmodels.VerificationPerson.objects.all().order_by('code'),
        label='Поверитель'
    )

    for_all = forms.BooleanField(
        required=False,
        label="Вывести для всех"
    )


class MocInUseForm(forms.Form):

    moc_name = forms.CharField(
        widget=forms.TextInput(),
        label='Введите тип СИ',
        max_length=20,
    )


class MemorandumForm(forms.Form):

    start_date = forms.DateField(
        label='Дата начала месяца поверки',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    workshop = forms.CharField(
        widget=forms.TextInput(),
        label='Цех',
        max_length=20,
    )

    brigade = forms.CharField(
        widget=forms.TextInput(),
        label='Бригада',
        max_length=20,
    )


class EconomVerifCostsPeriodForm(forms.Form):
    STATUS_CHOICES = [
        ('month', 'За месяц'),
        ('year', 'За год'),
    ]

    period = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.RadioSelect,
        label="Период",
        required=True
    )

    start_date = forms.DateField(
        label='Дата начала периода',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )


class EconomRefForm(forms.Form):

    start_date = forms.DateField(
        label='Дата начала года',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )


class EconomVerifStandartsForm(forms.Form):
    STATUS_CHOICES = [
        ('month', 'За месяц'),
        ('year', 'За год'),
    ]

    period = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.RadioSelect,
        label="Период",
        required=True
    )

    start_date = forms.DateField(
        label='Дата начала периода',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'date'}),
        initial=datetime.date.today,
    )

    class DepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    department = DepartmentChoiceField(
        hmodels.Department.objects.all().order_by('workshop'),
        label='Подразделение'
    )
