from django.db import models
from ..handbooks import models as hmodels
from django.utils.translation import gettext_lazy as _


class MocList(models.Model):
    """
    Общий список всех средств измерения
    """
    moc_type = models.ForeignKey(
        hmodels.MocType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='moc_list')

    factory_number = models.CharField(
        verbose_name='Заводской номер',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    inv_number = models.CharField(
        verbose_name='Инвентарный номер',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    change_type = models.ForeignKey(
        hmodels.ChangeType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='moc_list')

    moc_group = models.ForeignKey(
        hmodels.MocGroup,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='moc_list')

    class SignOR(models.TextChoices):
        WORKING = 'Р', _('Рабочий')
        EXEMPLARY = 'О', _('Образцовый')

    sign_o_r = models.CharField(
        verbose_name='Признак',
        max_length=1,
        choices=SignOR.choices,
        default=SignOR.WORKING,
    )

    class SignOM(models.TextChoices):
        DEFAULT = 'О', _('Основной')
        LOWVALUABLE = 'М', _('Малоценный')
        BUILTIN = 'В', _('Встроенный')

    sign_o_m = models.CharField(
        verbose_name='Признак',
        max_length=1,
        choices=SignOM.choices,
        default=SignOM.LOWVALUABLE,
    )

    verification_period = models.IntegerField(
        verbose_name='Период поверки(кол-во месяцев)',
        null=True,
        blank=True,
        default=0
    )

    verification_department = models.ForeignKey(
        hmodels.VerificationDepartment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='moc_list')

    class VerificationType(models.TextChoices):
        GOVERNMENTAL = 'Г', _('Государственная')
        DEPARTMENTAL = 'В', _('Ведомственная')

    verification_type = models.CharField(
        verbose_name='Вид поверки',
        max_length=1,
        choices=VerificationType.choices,
        default=VerificationType.GOVERNMENTAL,
    )


class MocMetals(models.Model):
    """
    Содержание в СИ драгметаллов
    """
    inv_number = models.CharField(
        verbose_name='Инвентарный номер',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    precious_metals = models.ForeignKey(
        hmodels.PreciousMetals,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='moc_metals')

    metal_amount = models.DecimalField(
        verbose_name='Содержание металла',
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=5
    )

    moc_list = models.ForeignKey(
        MocList,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='moc_metals')


class VerificationInfo(models.Model):
    """
    Сведения о поверках приборов
    """
    inv_number = models.CharField(
        verbose_name='Инвентарный номер',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    entry_date = models.DateField(
        verbose_name='Дата поступления на поверку',
        null=True,
        blank=True,
    )

    verification_date = models.DateField(
        verbose_name='Дата поверки',
        null=True,
        blank=True,
    )

    workshop_issue_date = models.DateField(
        verbose_name='Дата выдачи в цех',
        null=True,
        blank=True,
    )

    verification_result = models.CharField(
        verbose_name='Результат поверки',
        null=True,
        blank=True,
        max_length=100,
        default=''
    )

    verification_document_num = models.CharField(
        verbose_name='Номер документа о поверке',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    verification_person = models.ForeignKey(
        hmodels.VerificationPerson,
        on_delete=models.CASCADE,
        related_name='verification_info',
        null=True,
        blank=True,)

    verification_sign = models.ForeignKey(
        hmodels.VerificationSign,
        on_delete=models.CASCADE,
        related_name='verification_info',
        null=True,
        blank=True,)

    moc_list = models.ForeignKey(
        MocList,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='verification_info')


class RepairInfo(models.Model):
    """
    Сведения о ремонтах
    """
    inv_number = models.CharField(
        verbose_name='Инвентарный номер',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    entry_date = models.DateField(
        verbose_name='Дата выдачи',
        null=True,
        blank=True,
    )

    entry_repair_date = models.DateField(
        verbose_name='Дата выдачи в ремонт',
        null=True,
        blank=True,
    )

    repair_date = models.DateField(
        verbose_name='Дата ремонта',
        null=True,
        blank=True,
    )

    class RepairType(models.TextChoices):
        CURRENT = '4', _('Текущий')
        LONGTERM = '7', _('Долгосрочный')

    repair_type = models.CharField(
        verbose_name='Вид ремонта',
        max_length=1,
        choices=RepairType.choices,
        default=RepairType.CURRENT,
    )

    repair = models.ForeignKey(
        hmodels.Repair,
        on_delete=models.CASCADE,
        related_name='repair_info',
        null=True,
        blank=True,)

    repair_code = models.ForeignKey(
        hmodels.RepairCode,
        on_delete=models.CASCADE,
        related_name='repair_info',
        null=True,
        blank=True,)

    repair_department = models.ForeignKey(
        hmodels.RepairDepartment,
        on_delete=models.CASCADE,
        related_name='repair_info',
        null=True,
        blank=True,)

    instrument_failure = models.ForeignKey(
        hmodels.InstrumentFailure,
        on_delete=models.CASCADE,
        related_name='repair_info',
        null=True,
        blank=True,)

    moc_list = models.ForeignKey(
        MocList,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='repair_info')


class DeviceLocation(models.Model):
    """
    Места закрепления прибора
    """
    inv_number = models.CharField(
        verbose_name='Инвентарный номер',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    department = models.ForeignKey(
        hmodels.Department,
        on_delete=models.CASCADE,
        related_name='device_location',
        null=True,
        blank=True,)

    entry_date = models.DateField(
        verbose_name='Дата',
        null=True,
        blank=True,
    )

    moc_list = models.ForeignKey(
        MocList,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='device_location')


class DeviceStatusDate(models.Model):
    """
    Статус прибора
    """
    inv_number = models.CharField(
        verbose_name='Инвентарный номер',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    device_status = models.ForeignKey(
        hmodels.DeviceStatus,
        on_delete=models.CASCADE,
        related_name='device_status_date',
        null=True,
        blank=True,)

    status_date = models.DateField(
        verbose_name='Дата статуса',
        null=True,
        blank=True,
    )

    moc_list = models.ForeignKey(
        MocList,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='device_status_date')


class DeviceStation(models.Model):
    """
    Оборудование, на котором установлен данный СИ
    в качестве индикатора
    """
    inv_number = models.CharField(
        verbose_name='Инвентарный номер',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    station_inv_number = models.CharField(
        verbose_name='Инвентарный номер оборудовния',
        null=True,
        blank=True,
        max_length=20,
        default=''
    )

    station_name = models.CharField(
        verbose_name='Название оборудования',
        null=True,
        blank=True,
        max_length=50,
        default=''
    )

    moc_list = models.OneToOneField(
        MocList,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='device_station')
