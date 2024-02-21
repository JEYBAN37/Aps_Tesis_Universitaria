from rest_framework import serializers
from aps_api.models.familyContext import FamilyContext


class FamilyContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyContext
        fields = '__all__'

