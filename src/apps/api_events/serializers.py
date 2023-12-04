from rest_framework import serializers
from apps.coordinators.models import Coordinators

class CoordinatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinators
        fields = '__all__'