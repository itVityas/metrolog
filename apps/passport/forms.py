from django import forms
from . import models


class MocListForm(forms.ModelForm):

    class Meta:
        model = models.MocList
        fields = ("__all__")