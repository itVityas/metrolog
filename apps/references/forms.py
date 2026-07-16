from django import forms
from ..handbooks import models as hmodels
from django.forms import ModelChoiceField
import datetime


class MocPresenceForm(forms.Form):

    class DepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    class ChangeTypeChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    change_type = ChangeTypeChoiceField(
        hmodels.ChangeType.objects.all(),
        label='Вид измерения'
    )

    department = DepartmentChoiceField(
        hmodels.Department.objects.all(),
        label='Подразделение'
    )


class VerificationLogForm(forms.Form):

    class ChangeTypeChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    change_type = ChangeTypeChoiceField(
        hmodels.ChangeType.objects.all(),
        label='Вид измерения'
    )

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
        hmodels.Department.objects.all(),
        label='Подразделение'
    )


class MocIndicatorsForm(forms.Form):

    class DepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    department = DepartmentChoiceField(
        hmodels.Department.objects.all(),
        label='Подразделение'
    )


class CompletedWorksForm(forms.Form):

    class DepartmentChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return "%s" % obj.name

    department = DepartmentChoiceField(
        hmodels.Department.objects.all(),
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
        hmodels.RepairDepartment.objects.all(),
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
        hmodels.VerificationPerson.objects.all(),
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
