from rest_framework import serializers
from aps_api.models.channelEntity import ChannelEntity


class ChannelEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelEntity
        fields = '__all__'
