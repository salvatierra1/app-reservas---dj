from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Services
from django.views import generic
from django.contrib import messages

# Create your views here.
class ServicesCreateView(generic.CreateView):
    model= Services
    fields= '__all__'
    template_name = 'services/create.html'
    success_url = reverse_lazy('apps.services:list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"¡El servicio '{self.object.name}' fue creado correctamente!")
        return response

class ServicesListView(generic.ListView):
    model= Services
    template_name = 'services/list.html'
    context_object_name = 'services'
    