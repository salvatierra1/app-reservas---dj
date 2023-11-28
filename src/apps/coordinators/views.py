from django.shortcuts import render
from .models import Coordinators
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.


class CoordinatorsCreateView(generic.CreateView):
    model= Coordinators
    fields= '__all__'
    template_name = 'coordinators/create.html'
    success_message = "¡El coordinador '%(name)s' fue creado correctamente!"
    success_url = reverse_lazy('apps.coordinators:list')
    
class CoordinatorsUpdateView(generic.UpdateView):
    model = Coordinators
    fields= '__all__'
    template_name = 'coordinators/update.html'
    success_message = "¡El coordinador '%(name)s' fue actualizado correctamente!"
    success_url = reverse_lazy('apps.coordinators:list')
    
class CoordinatorsListView(generic.ListView):
    model= Coordinators
    template_name = 'coordinators/list.html'
    context_object_name = 'coordinators'
    