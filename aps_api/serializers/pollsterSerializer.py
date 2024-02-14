from rest_framework import serializers
from aps_api.models.pollster import Pollster


class PollsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pollster
        fields = '__all__'
