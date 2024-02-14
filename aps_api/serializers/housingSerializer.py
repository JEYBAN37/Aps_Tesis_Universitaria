from rest_framework import serializers
from aps_api.models.housing import Housing


class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = '__all__'
