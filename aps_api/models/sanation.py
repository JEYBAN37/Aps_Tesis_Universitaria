from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .housing import Housing
from aps_api.resources import Enums


class Sanation(models.Model):
    serial_id = models.AutoField(primary_key=True)
    housing = models.OneToOneField(Housing, on_delete=models.CASCADE)
    source_supply_water = models.IntegerField(choices=Enums.OPTIONS_SS)  # 75
    ss_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 76
    disposal_system = models.IntegerField(choices=Enums.OPTIONS_DS)  # 77
    ds_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 78
    Wastewater = models.IntegerField(choices=Enums.OPTIONS_W)  # 79
    w_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 80
    Solid_waste = models.IntegerField(choices=Enums.OPTIONS_SW)  # 81
    sw_descripcion = models.CharField(max_length=30, null=True, blank=True)
    #  Esta Revisado

    #  Fuera de datos requeridos
    hygiene = models.IntegerField(choices=Enums.OPTIONS_YN)
    hygiene_food = models.IntegerField(choices=Enums.OPTIONS_YN)
    cleanliness = models.IntegerField(choices=Enums.OPTIONS_YN)
    handwashing = models.IntegerField(choices=Enums.OPTIONS_YN)
    hygiene_elements = models.IntegerField(choices=Enums.OPTIONS_HE)
    brushed = models.IntegerField(choices=Enums.OPTIONS_B)
