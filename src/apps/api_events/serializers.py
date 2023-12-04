from rest_framework import serializers
from apps.coordinators.models import Coordinators

class CoordinatorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinators
        fields = ['id', 'name']
    
class CoordinatorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinators
        fields = '__all__'