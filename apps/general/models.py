from django.db import models
from ..accounts.models import User


class UserSettings(models.Model):
    """
    Пользовательские настройки
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='usersettings')

    pagination_size = models.IntegerField(
        verbose_name='Количество строк',
        null=True,
        blank=True,
        default=10
    )
