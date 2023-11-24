from django.shortcuts import render
from .models import Employes
from django.views import generic

# Create your views here.

class EmployesCreateView(generic.CreateView):
    model= Employes
    fields= '__all__'
    template_name = 'employes/create.html'