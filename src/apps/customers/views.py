from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Customers
from django.views import generic

# Create your views here.
class CustomersCreateView(generic.CreateView):
    model= Customers
    fields= '__all__'
    template_name = 'customers/create.html'
    success_message = "¡El cliente '%(name)s' fue creado correctamente!"
    success_url = reverse_lazy('apps.customers:list')

class CustomersUpdateView(generic.UpdateView):
    model= Customers
    fields= '__all__'
    template_name = 'customers/update.html'
    success_message = "¡El cliente '%(name)s' fue actualizado correctamente!"
    success_url = reverse_lazy('apps.customers:list')
    
class CustomersListView(generic.ListView):
    model= Customers
    template_name = 'customers/list.html'
    context_object_name = 'customers'
    
    
