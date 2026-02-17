from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.accounts.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Username',
        help_text='Имя пользователя'
        )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Is staff',
        help_text='Является администратором'
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='User created',
        help_text='Дата, время создания пользователя'
        )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='User last updated',
        help_text='Дата, время последнего изменения пользователя'
        )
    is_active = models.BooleanField(
        default=True
        )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
