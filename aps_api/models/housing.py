from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .infoGeneral import InfoGeneral
from aps_api.resources import Enums


class Housing(models.Model):
    serial_id = models.AutoField(primary_key=True)
    info_general = models.OneToOneField(InfoGeneral, on_delete=models.CASCADE)
    home_type = models.IntegerField(choices=Enums.OPTIONS_HT)  # 54
    ht_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 55
    structural_material = models.IntegerField(choices=Enums.OPTIONS_SM)  # 56
    sm_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 57
    floor_material = models.IntegerField(choices=Enums.OPTIONS_FM)  # 58
    fm_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 59
    roofing_material = models.IntegerField(choices=Enums.OPTIONS_RM)  # 60
    rm_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 61
    bedrooms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(50)])  # 62
    overcrowding = models.IntegerField(choices=Enums.OPTIONS_YN)  # 63
    irrigation_scenarios = models.IntegerField(choices=Enums.OPTIONS_SI, null=True)  # 64
    access_to_home = models.IntegerField(choices=Enums.OPTIONS_AC)  # 65
    food_source = models.IntegerField(choices=Enums.OPTIONS_FS)  # 66
    fs_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 67
    transmitting_vectors = models.IntegerField(choices=Enums.OPTIONS_YN)  # 68
    tv_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 69
    outdoor_environments = models.IntegerField(choices=Enums.OPTIONS_OE)  # 70//Acomulador
    oe_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 71
    economic_activities = models.IntegerField(choices=Enums.OPTIONS_YN)  # 72
    animals = models.IntegerField(choices=Enums.OPTIONS_A)  # 73
    a_descripcion = models.CharField(max_length=30, null=True, blank=True)  # 74
# Esta Revisado


