from rest_framework import serializers
from aps_api.models.welfare import Welfare


class WelfareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welfare
        fields = '__all__'
