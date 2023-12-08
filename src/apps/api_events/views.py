from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.coordinators.models import Coordinators
from apps.services.models import Services
from apps.employees.models import Employees
from .serializers import CoordinatorsListSerializer, CoordinatorsDetailSerializer

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
    # serializer_class = ServicesListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ServicesRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    # serializer_class = ServicesDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    
    
# Api Employees

class EmployeesListAPIView(generics.ListAPIView):
    queryset = Employees.objects.all()
    # serializer_class = EmployeesListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class EmployeesRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employees.objects.all()
    # serializer_class = EmployeesDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  