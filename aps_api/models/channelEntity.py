from django.db import models
from .representative import Representative


class ChannelEntity(models.Model):
    serial_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    campus = models.CharField(max_length=15)  # 17
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, null=True, blank=True)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)
# Esta Revisado
