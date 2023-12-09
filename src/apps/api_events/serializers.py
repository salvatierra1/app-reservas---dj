from rest_framework import serializers
from apps.coordinators.models import Coordinators
from apps.employees.models import Employees
from apps.services.models import Services

class CoordinatorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinators
        fields = ['id', 'name']
    
class CoordinatorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinators
        fields = '__all__'
        
class EmployeesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'name']
        
class EmployeesDetailSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Employees
        fields = '__all__'
        
class ServicesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'name']
        
class ServicesDetailSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Services
        fields = '__all__'