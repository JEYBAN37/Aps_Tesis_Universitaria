from rest_framework import serializers
from aps_api.models.sanation import Sanation


class SanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanation
        fields = '__all__'
