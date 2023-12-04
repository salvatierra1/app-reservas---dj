from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.coordinators.models import Coordinators
from apps.services.models import Services
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