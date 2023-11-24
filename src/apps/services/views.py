from django.shortcuts import render
from .models import Services
from django.views import generic
# Create your views here.



class ServicesCreateView(generic.CreateView):
    model= Services
    fields= '__all__'
    template_name = 'services/create.html'