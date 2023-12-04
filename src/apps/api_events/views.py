from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.coordinators.models import Coordinators
from .serializers import CoordinatorsSerializer

# Create your views here.

class CoordinatorsListAPIView(generics.ListAPIView):
    queryset = Coordinators.objects.all()
    serializer_class = CoordinatorsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
