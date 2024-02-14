from rest_framework import serializers
from aps_api.models.pipelines import Pipelines


class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipelines
        fields = '__all__'
