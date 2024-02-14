from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .pollster import Pollster
from .housing import Housing
from aps_api.resources import Enums


class InfoGeneral(models.Model):
    serial_id = models.AutoField(primary_key=True)
    housing = models.OneToOneField(Housing, on_delete=models.CASCADE)
    type_register = models.IntegerField(default=1)  # 0
    number_register = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])  # 1
    consent = models.IntegerField(choices=Enums.OPTIONS_YN)  # 2
    departament = models.CharField(max_length=2)  # 3
    zonal_unit = models.CharField(max_length=7)  # 4
    municipality = models.CharField(max_length=5)  # 5
    territory = models.CharField(max_length=3)  # 6
    microterritory = models.CharField(max_length=4)  # 7
    name_branding = models.CharField(max_length=200)  # 8
    address = models.CharField(max_length=200, null=True, blank=True)  # 9
    longitud = models.DecimalField(max_digits=11, decimal_places=8)  # 10
    latitud = models.DecimalField(max_digits=10, decimal_places=8)  # 11
    home_location = models.CharField(max_length=200, null=True, blank=True)  # 12
    id_familia = models.CharField(max_length=32, null=True, blank=True)  # 13 Pendiente Validate
    estratum = models.IntegerField(choices=Enums.OPTIONS_STR)  # 14
    households = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])  # 15
    num_families = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])  # 16
    people = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])  # 17
    basic_team = models.CharField(max_length=27)   # 18  Codificacion pendiente
    id_primary_provider = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])  # 19
    # Codificacion pendiente
    pollster = models.ForeignKey(Pollster, on_delete=models.CASCADE)  # Los codigos abscritos son 20-21
    id_ficha = models.CharField(max_length=27)   # 22  pendiente codificacion
    creation_date = models.DateTimeField(auto_now_add=True)  # 23
    # pets = models.ForeignKey("Pets", on_delete=models.CASCADE)
# Esta Revisado Pendiente Algunos Ajustes
