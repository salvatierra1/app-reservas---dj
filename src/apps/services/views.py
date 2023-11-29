from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Services
from django.views import generic
# Create your views here.

class ServicesCreateView(generic.CreateView):
    model= Services
    fields= '__all__'
    template_name = 'services/create.html'
    success_message = "¡El servicio '%(name)s' fue creado correctamente!"
    success_url = reverse_lazy('apps.services:list')

class ServicesListView(generic.ListView):
    model= Services
    template_name = 'services/list.html'
    context_object_name = 'services'
    