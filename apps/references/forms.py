from django import forms
from ..handbooks import models as hmodels
from django.forms import ModelChoiceField


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
