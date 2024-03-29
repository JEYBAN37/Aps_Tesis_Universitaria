from django.db import models
from .channelEntity import ChannelEntity
from .member import Member


class Pipelines(models.Model):
    serial_id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(ChannelEntity, on_delete=models.CASCADE)
    person = models.ForeignKey(Member, on_delete=models.CASCADE)
    channel = models.CharField(max_length=150)
