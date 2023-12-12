from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.coordinators.models import Coordinators
from apps.customers.models import Customers
from apps.services.models import Services
from apps.employees.models import Employees
from apps.bookings.models import Bookings
from .serializers import BookingsDetailSerializer, BookingsListSerializer, CoordinatorsListSerializer, CoordinatorsDetailSerializer, CustomersDetailSerializer, CustomersListSerializer, EmployeesDetailSerializer, EmployeesListSerializer, ServicesDetailSerializer, ServicesListSerializer

# Create your views here.

# Api coordinators

class CoordinatorsListAPIView(generics.ListAPIView):
    queryset = Coordinators.objects.all()
    serializer_class = CoordinatorsListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class CoordinatorsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Coordinators.objects.all()
    serializer_class = CoordinatorsDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    

# Api Services

class ServicesListAPIView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ServicesRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    
    
# Api Employees

class EmployeesListAPIView(generics.ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class EmployeesRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  

# Api Bookings

class BookingsListAPIView(generics.ListAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingsListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class BookingsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingsDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  
    
# Api Customers

class CustomersListAPIView(generics.ListAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class CustomersRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  