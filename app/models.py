"""
Definition of models.
"""

from django.db import models

# Create your models here.
from django.db import models
# Неправильная таблица
class LeasingRecord(models.Model):
    contract_number = models.CharField(max_length=100, unique=True)
    client_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'leasing_records'

    def __str__(self):
        return f"{self.contract_number} - {self.client_name}"


class AllTechnic(models.Model):
    TYPE_TECHNIC = [
        ('Truck', 'Грузовики и прицепы'),
        ('Dump', 'Самосвалы'),
        ('Car', 'Легковой'),
        ('Earthmover', 'Бульдозер,Экскаватор, Грейдер, Скрепер'),
        ('LCVs', 'Коммерческие грузовики'),
        ('Logging', 'Лесозаготовка'),
        ('Equipment', 'Оборудование'),
     # другие типы
    ]
    TYPE_BRANCHES = [
        ('Longhaul', 'Междугородные перевозки'),
        ('Roadbuilding', 'Дорожное строительство'),
        
        ('Career', 'Разработка карьера'),
        ('Cityhaul', 'Грузовые перевозки по городу'),
        ('Logging', 'Лесозаготовка'),
        ('Construction', 'Строительство'),
     # другие типы
    ]

    
    what = models.CharField(max_length=100, choices=TYPE_TECHNIC, verbose_name='Тип техники')
    branch = models.CharField(max_length=100, choices=TYPE_BRANCHES, verbose_name='Отрасль')
    name = models.CharField(max_length=100, verbose_name='Название')
    production_year = models.IntegerField(verbose_name='Год выпуска')  # Исправлено на IntegerField
    motor_hours = models.IntegerField(verbose_name='Моточасы')  # Исправлено на IntegerField
    location = models.CharField(max_length=100, verbose_name='Местоположение')  # Переименовано where → location
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')  # Исправлено на DecimalField
    quantity = models.IntegerField(verbose_name='Количество')  # Исправлена опечатка
    info = models.TextField(verbose_name='Дополнительная информация')  # TextField вместо CharField
    ready = models.BooleanField(default=False, verbose_name='Готовность')  # BooleanField для да/нет
    contact = models.CharField(max_length=50, verbose_name='Контакт')

    class Meta:
        
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

    def __str__(self):
        return f"{self.what} ({self.name})"