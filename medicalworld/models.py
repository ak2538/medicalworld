from django.db import models



class MedEquipment(models.Model):
    EquipmentType = models.CharField(max_length=200)
    NumberOfItems = models.IntegerField(default=0)
    Price = models.DecimalField(max_digits=6, decimal_places=2)