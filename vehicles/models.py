from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_service = models.BooleanField(default=False, blank=True, verbose_name='Является сотрудником сервисной компании')
    service_company = models.ForeignKey(to='service.ServiceCompany',blank=True, null=True, on_delete=models.PROTECT, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.user.username} {self.is_service}'
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Technic(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'

class Engine(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'

class Transmission(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'

class DrivingBridge(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущих мостов'

class ControlledBridge(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемых мостов'

class Car(models.Model):
    car_number = models.CharField(unique=True, max_length=12, verbose_name='Зав. № машины')
    technic = models.ForeignKey(Technic, on_delete=models.CASCADE, verbose_name='Модель техники')
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, verbose_name='Модель двигателя')
    engine_number = models.CharField(max_length=12, verbose_name='Зав. № двигателя')
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, verbose_name='Модель трансмиссии')
    transmission_number = models.CharField(max_length=12, verbose_name='Зав. № трансмиссии')
    driving_bridge = models.ForeignKey(DrivingBridge, on_delete=models.CASCADE, verbose_name='Модель ведущего моста')
    driving_bridge_number = models.CharField(max_length=12, verbose_name='Зав. № ведущего моста')
    controlled_bridge = models.ForeignKey(ControlledBridge, on_delete=models.CASCADE, verbose_name='Модель управляемого моста')
    controlled_bridge_number = models.CharField(max_length=12, verbose_name='Зав. № управляемого моста')
    delivery_contract = models.CharField(max_length=20, verbose_name='Договор поставки №, дата')
    date_shipment = models.DateField(default=datetime.now, verbose_name='Дата отгрузки с завода')
    consignee = models.CharField(max_length=200, verbose_name='Грузополучатель (конечный потребитель)')
    delivery_address = models.CharField(max_length=200, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(blank=False,verbose_name='Комплектация (доп. опции)', default="Стандарт")
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    service_company = models.ForeignKey(to='service.ServiceCompany', on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.car_number}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'