from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from aps_api.resources import Enums
from .family import Family


class Member(models.Model):
    serial_id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    present_person = models.IntegerField(choices=Enums.OPTIONS_YN)
    type_register = models.IntegerField(default=1)  # 0
    consent = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])  # 1
    name = models.CharField(max_length=60)  # 2
    second_name = models.CharField(max_length=60)  # 3
    last_name = models.CharField(max_length=60)  # 4
    second_last_name = models.CharField(max_length=60)  # 5
    type_id = models.CharField(max_length=15, choices=Enums.TYPE_ID)  # 6
    id = models.CharField(max_length=15)  # 7
    date_birth = models.DateTimeField(auto_now_add=True)  # 8
    sex = models.IntegerField(choices=Enums.SEX)  # 9
    role = models.IntegerField(choices=Enums.ROLE)  # 10
    weight = models.CharField(max_length=5, null=True, blank=True)  # 27
    size = models.CharField(max_length=5, null=True, blank=True)  # 28

    #  Dato no pedidios en informe
    affiliation_regime = models.CharField(max_length=5)  # Pendiente
    age = models.CharField(max_length=2)
#  Esta Revisado Pendiente Algunos Ajustes
