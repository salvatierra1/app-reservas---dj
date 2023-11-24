from django.shortcuts import render
from .models import Coordinators
from django.views import generic
# Create your views here.


class CoordinatorsCreateView(generic.CreateView):
    model= Coordinators
    fields= '__all__'
    template_name = 'coordinators/create.html'