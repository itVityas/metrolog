from django import forms
from ..models import DeviceStatus


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
