from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .infoGeneral import InfoGeneral
from .familyContext import FamilyContext
from .welfare import Welfare
from aps_api.resources import Enums


class Family(models.Model):
    serial_id = models.AutoField(primary_key=True)  # 10
    info_general = models.ForeignKey(InfoGeneral, on_delete=models.CASCADE)
    welfare = models.OneToOneField(Welfare, on_delete=models.CASCADE)
    family_context = models.OneToOneField(FamilyContext, on_delete=models.CASCADE)
    family_type = models.IntegerField(choices=Enums.OPTIONS_FT)  # 24
    num_member = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])  # 25
    family_graphic = models.IntegerField(choices=Enums.OPTIONS_FG)  # 26
    apgar = models.IntegerField(choices=Enums.OPTIONS_APGAR)  # 27
    carer = models.IntegerField(choices=Enums.OPTIONS_YN)  # 28
    zarit = models.IntegerField(choices=Enums.OPTIONS_ZT, null=True)  # 29
    ecomapa = models.IntegerField(choices=Enums.OPTIONS_ECO)  # 30
# Esta Revisado
