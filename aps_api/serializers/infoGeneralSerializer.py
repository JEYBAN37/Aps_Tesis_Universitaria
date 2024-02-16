from rest_framework import serializers
from aps_api.models.infoGeneral import InfoGeneral


class InfoGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoGeneral
        fields = '__all__'


