from django.db import models
from aps_api.resources import Enums
from .family import Family


class Member(models.Model):
    serial_id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)  # 49 50
    last_name = models.CharField(max_length=250)  # 51 52
    age = models.CharField(max_length=2)  #
    date_birth = models.DateTimeField(auto_now_add=True)  # 55
    type_id = models.CharField(max_length=15, choices=Enums.TYPE_ID)  # 53
    id = models.CharField(max_length=15)  # 54
    sex = models.IntegerField(choices=Enums.SEX)  # 56
    role = models.IntegerField(choices=Enums.ROLE)  # 57
    weight = models.CharField(max_length=5)  # 74
    size = models.CharField(max_length=5)  # 74
    affiliation_regime = models.CharField(max_length=5)  # Pendiente