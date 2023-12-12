from rest_framework import serializers
from apps.coordinators.models import Coordinators
from apps.employees.models import Employees
from apps.services.models import Services
from apps.customers.models import Customers
from apps.bookings.models import Bookings

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
        
class CustomersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'name']
        
class CustomersDetailSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Customers
        fields = '__all__'
        
class BookingsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ['id', 'booking_date']
    
class BookingsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'