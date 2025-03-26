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


class All_tecnic(models.Model):
    what = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    production_year = models.DateField()
    m_hours = models.CharField(max_length=30)      
    where = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    guantity = models.CharField(max_length=50)
    info = models.CharField(max_length=200)
    ready = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
        
    
    class Meta:
        db_table = 'all_tecnic'
# ???

        verbose_name = 'Техника'
        verbose_name_plural = 'Договоры'

    def __str__(self):
        return f"{self.contract_number} - {self.client_name}"