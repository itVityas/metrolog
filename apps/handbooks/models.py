from django.db import models


class MocGroup(models.Model):
    """
    Наименование группы средств измерения
    (Группы СИ)
    """
    type = models.CharField(
        verbose_name='Вид измерения',
        null=True,
        blank=True,
        max_length=4,
        default=''
    )
    group = models.IntegerField(
        verbose_name='Группа СИ(код)',
        null=True,
        blank=True,
        default=0
    )
    name = models.CharField(
        verbose_name='Наименование группы СИ',
        null=True,
        blank=True,
        max_length=100,
        default=''
    )


class Department(models.Model):
    """
    Место закрепления
    """
    workshop = models.IntegerField(
        verbose_name='Цех',
        null=False,
        blank=False
    )
    brigade = models.IntegerField(
        verbose_name='Бригада',
        null=True,
        blank=True
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
    Характер ремонта
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
        verbose_name='Признак',
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
    code = models.CharField(
        verbose_name='Код',
        null=False,
        blank=False,
        max_length=10
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
        verbose_name='Наименование',
        null=False,
        blank=False,
        max_length=50
    )


class ChangeType(models.Model):
    """
    Вид измерения
    """
    code = models.CharField(
        verbose_name='Код вида измерения',
        null=False,
        blank=False,
        max_length=10
    )
    name = models.CharField(
        verbose_name='Наименование',
        null=False,
        blank=False,
        max_length=100
    )


class MocType(models.Model):
    """
    Данные по типам СИ
    """
    type = models.CharField(
        verbose_name='Тип СИ',
        null=True,
        blank=True,
        max_length=50
    )
    code = models.IntegerField(
        verbose_name='Код',
        null=True,
        blank=True
    )
    accurancy = models.DecimalField(
        verbose_name='Точность',
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=5
    )
    cost = models.DecimalField(
        verbose_name='Стоимость госповерки',
        null=True,
        blank=True,
        max_digits=9,
        decimal_places=2
    )
    min_limit = models.DecimalField(
        verbose_name='Мин. предел измерения',
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=5
    )
    max_limit = models.DecimalField(
        verbose_name='Макс. предел измерения',
        null=True,
        blank=True,
        max_digits=12,
        decimal_places=5
    )
    min_measurement = models.CharField(
        verbose_name='Единица изм. мин. предела',
        null=True,
        blank=True,
        max_length=5
    )
    max_measurement = models.CharField(
        verbose_name='Единица изм. макс. предела',
        null=True,
        blank=True,
        max_length=5
    )
    standart_verification = models.DecimalField(
        verbose_name='Норма поверки',
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=1
    )
    standart_repair = models.DecimalField(
        verbose_name='Норма ремонта',
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=1
    )
    rank_verification = models.IntegerField(
        verbose_name='Разряд поверителя',
        null=True,
        blank=True
    )
    rank_repair = models.IntegerField(
        verbose_name='Разряд ремонтника',
        null=True,
        blank=True
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
        verbose_name='Мин. предел измерения',
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=5
    )
    max_limit = models.DecimalField(
        verbose_name='Макс. предел измерения',
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=5
    )
    min_measurement = models.CharField(
        verbose_name='Единица изм. мин. предела',
        null=False,
        blank=False,
        max_length=5
    )
    max_measurement = models.CharField(
        verbose_name='Единица изм. макс. предела',
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
    code = models.CharField(
        verbose_name='Код',
        null=False,
        blank=False,
        max_length=10
    )
    sign = models.IntegerField(
        verbose_name='Разряд',
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
