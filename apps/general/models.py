from django.db import models


# Create your models here.
class UserSettings(models.Model):
    """
    Пользовательские настройки
    """
    pagination_size = models.IntegerField(
        verbose_name='Количество строк',
        null=True,
        blank=True,
        default=10
    )