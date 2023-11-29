from django.shortcuts import render
from .models import Bookings
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

class BookingsCreateView(generic.CreateView):
    model= Bookings
    fields= '__all__'
    template_name = 'bookings/create.html'
    success_message = "¡La reserva '%(name)s' fue creada correctamente!"
    success_url = reverse_lazy('apps.bookings:list') 
       
class BookingsUpdateView(generic.UpdateView):
    model = Bookings
    fields= '__all__'
    template_name = 'bookings/update.html'
    success_message = "¡La reserva '%(name)s' fue actualizada correctamente!"
    success_url = reverse_lazy('apps.bookings:list')   

class BookingsDeleteView(generic.DeleteView):
    model = Bookings
    success_url = reverse_lazy("bookings:listar")
    template_name = 'bookings/delete.html'  
    
class BookingsListView(generic.ListView):
    model= Bookings
    template_name = 'bookings/list.html'
    context_object_name = 'bookings'   
    

    
 
    