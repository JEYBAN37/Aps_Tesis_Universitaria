from rest_framework import serializers
from aps_api.models.representative import Representative


class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        fields = '__all__'
