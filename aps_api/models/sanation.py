from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .housing import Housing
from aps_api.resources import Enums


class Sanation(models.Model):
    serial_id = models.AutoField(primary_key=True)
    housing = models.OneToOneField(Housing, on_delete=models.CASCADE)
    source_supply = models.IntegerField(choices=Enums.OPTIONS_SS)  # 96
    ss_descripcion = models.CharField(max_length=50, null=True, blank=True)
    disposal_system = models.IntegerField(choices=Enums.OPTIONS_DS)  # 82
    ds_descripcion = models.CharField(max_length=50, null=True, blank=True)
    Wastewater = models.IntegerField(choices=Enums.OPTIONS_W)  # 82
    w_descripcion = models.CharField(max_length=50, null=True, blank=True)
    Solid_waste = models.IntegerField(choices=Enums.OPTIONS_SW)  # 82
    sw_descripcion = models.CharField(max_length=50, null=True, blank=True)
    hygiene = models.IntegerField(choices=Enums.OPTIONS_YN)
    hygiene_food = models.IntegerField(choices=Enums.OPTIONS_YN)
    cleanliness = models.IntegerField(choices=Enums.OPTIONS_YN)
    handwashing = models.IntegerField(choices=Enums.OPTIONS_YN)
    hygiene_elements = models.IntegerField(choices=Enums.OPTIONS_HE)
    brushed = models.IntegerField(choices=Enums.OPTIONS_B)
