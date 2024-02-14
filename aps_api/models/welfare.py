from django.db import models
from aps_api.resources import Enums


class Welfare(models.Model):
    serial_id = models.AutoField(primary_key=True)
    tenure = models.IntegerField(choices=Enums.OPTIONS_T)
    time_residence = models.CharField(max_length=250)
    permanence = models.IntegerField(choices=Enums.OPTIONS_TR)
    lgtbi = models.IntegerField(choices=Enums.OPTIONS_YN)
    life_style = models.IntegerField(choices=Enums.OPTIONS_LS )
    alternative_health = models.IntegerField(choices=Enums.OPTIONS_YN)