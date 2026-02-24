from django.db import models


class MocGroup(models.Model):
    """
    Группы СИ
    """
    type = models.IntegerField(
        verbose_name='Тип',
        null=False,
        blank=False
    )
    group = models.IntegerField(
        verbose_name='Группа',
        null=False,
        blank=False
    )
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=100
    )


class Department(models.Model):
    """
    Место закрепления
    """
    workshop = models.IntegerField(
        verbose_name='workshop',
        null=False,
        blank=False
    )
    brigade = models.IntegerField(
        verbose_name='brigade',
        null=False,
        blank=False
    )
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=100
    )
    is_active = models.BooleanField(
        verbose_name='Активно',
        null=False,
        blank=False,
        default=False
    )


class Repair(models.Model):
    """
    Статус ремонта
    """
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=50
    )


class PreciousMetals(models.Model):
    """
    Драгметаллы
    """
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=50
    )


class VerificationDepartment(models.Model):
    """
    Подразделения поверители
    """
    code = models.IntegerField(
        verbose_name='Код',
        null=False,
        blank=False
    )
    sign = models.IntegerField(
        verbose_name='Знак',
        null=False,
        blank=False
    )
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=100
    )
    is_active = models.BooleanField(
        verbose_name='Активно',
        null=False,
        blank=False
    )


class VerificationPerson(models.Model):
    """
    Поверители отдела
    """
    code = models.IntegerField(
        verbose_name='Код',
        null=False,
        blank=False
    )
    rank = models.IntegerField(
        verbose_name='Разряд',
        null=False,
        blank=False
    )
    fio = models.CharField(
        verbose_name='Фио',
        null=False,
        blank=False,
        max_length=100
    )
    is_active = models.BooleanField(
        verbose_name='Активен',
        null=False,
        blank=False,
        default=False
    )


class RepairCode(models.Model):
    """
    Категория ремонта
    """
    code = models.CharField(
        verbose_name='Код',
        null=False,
        blank=False,
        max_length=10
    )
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=100
    )


class InstrumentFailure(models.Model):
    """
    Отказ прибора
    """
    code = models.CharField(
        verbose_name='Код',
        null=False,
        blank=False,
        max_length=10
    )
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=100
    )


class DeviceStatus(models.Model):
    """
    Статус прибора
    """
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=50
    )


class ChangeType(models.Model):
    """
    Вид измерения
    """
    code = models.CharField(
        verbose_name='Код',
        null=False,
        blank=False,
        max_length=10
    )
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=100
    )


class MocType(models.Model):
    """
    Данные по типам СИ
    """
    type = models.CharField(
        verbose_name='Тип',
        null=False,
        blank=False,
        max_length=50
    )
    code = models.IntegerField(
        verbose_name='Код',
        null=False,
        blank=False
    )
    accurancy = models.DecimalField(
        verbose_name='Точность',
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=10
    )
    cost = models.DecimalField(
        verbose_name='Цена',
        null=False,
        blank=False,
        max_digits=9,
        decimal_places=2
    )
    min_limit = models.DecimalField(
        verbose_name='Мин. лимит',
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=5
    )
    max_limit = models.DecimalField(
        verbose_name='Макс. лимит',
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=5
    )
    min_measurement = models.CharField(
        verbose_name='Мин. измерение',
        null=False,
        blank=False,
        max_length=5
    )
    max_measurement = models.CharField(
        verbose_name='Макс. измерение',
        null=False,
        blank=False,
        max_length=5
    )
    standart_verification = models.DecimalField(
        verbose_name='Стандарт поверки',
        null=False,
        blank=False,
        max_digits=2,
        decimal_places=1
    )
    standart_repair = models.DecimalField(
        verbose_name='Стандартный ремонт',
        null=False,
        blank=False,
        max_digits=2,
        decimal_places=1
    )
    rank_verification = models.IntegerField(
        verbose_name='Разряд поверки',
        null=False,
        blank=False
    )
    rank_repair = models.IntegerField(
        verbose_name='Разряд ремонта',
        null=False,
        blank=False
    )


class UnitsMeasurement(models.Model):
    """
    Единицы измерения
    """
    code = models.CharField(
        verbose_name='Код',
        null=False,
        blank=False,
        max_length=10
    )
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=100
    )


class MocLimit(models.Model):
    """
    Пределы измерения
    """
    type = models.CharField(
        verbose_name='Тип',
        null=False,
        blank=False,
        max_length=50
    )
    min_limit = models.DecimalField(
        verbose_name='Мин. лимит',
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=5
    )
    max_limit = models.DecimalField(
        verbose_name='Макс. лимит',
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=5
    )
    min_measurement = models.CharField(
        verbose_name='Мин. измерение',
        null=False,
        blank=False,
        max_length=5
    )
    max_measurement = models.CharField(
        verbose_name='Макс. измерение',
        null=False,
        blank=False,
        max_length=5
    )


class VerificationSign(models.Model):
    """
    Признак поверки
    """
    code = models.CharField(
        verbose_name='Код',
        null=False,
        blank=False,
        max_length=10
    )
    name = models.CharField(
        verbose_name='Название',
        null=False,
        blank=False,
        max_length=100
    )


class RepairDepartment(models.Model):
    """
    Ремонтники отдела
    """
    code = models.IntegerField(
        verbose_name='Код',
        null=False,
        blank=False
    )
    sign = models.IntegerField(
        verbose_name='Знак',
        null=False,
        blank=False
    )
    name = models.CharField(
        verbose_name='Имя',
        null=False,
        blank=False,
        max_length=100
    )
    is_active = models.BooleanField(
        verbose_name='Активен',
        null=False,
        blank=False
    )
