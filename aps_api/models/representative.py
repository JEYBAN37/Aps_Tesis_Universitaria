from django.db import models


class Representative(models.Model):
    serial_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    id = models.CharField(max_length=15)  # 17
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, null=True, blank=True)
    job = models.CharField(max_length=30)
    role = models.CharField(max_length=50)  # 18