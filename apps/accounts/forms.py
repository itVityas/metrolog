from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import forms
from .models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username",)
