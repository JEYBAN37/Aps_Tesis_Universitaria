from rest_framework import serializers
from aps_api.models import InfoGeneral


class InfoSociambientalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoGeneral
        fields = '__all__'
