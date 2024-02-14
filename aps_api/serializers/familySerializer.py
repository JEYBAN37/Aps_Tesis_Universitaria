from rest_framework import serializers
from aps_api.models.family import Family


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'
