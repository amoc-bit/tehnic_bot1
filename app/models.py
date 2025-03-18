"""
Definition of models.
"""

from django.db import models

# Create your models here.
from django.db import models

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
