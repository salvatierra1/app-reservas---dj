from django.shortcuts import render
from apps.coordinators.models import Coordinators
from apps.customers.models import Customers
from apps.employees.models import Employees
from apps.services.models import Services
from .models import Bookings
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class BookingsCreateView(generic.CreateView):
    model= Bookings
    fields= '__all__'
    template_name = 'bookings/create.html'
    success_url = reverse_lazy('apps.bookings:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customers.objects.all()
        context['services'] = Services.objects.all()
        context['employees'] = Employees.objects.all()
        context['coordinators'] = Coordinators.objects.all()
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"¡La reserva fue creada correctamente!")
        return response
       
class BookingsUpdateView(generic.UpdateView):
    model = Bookings
    fields= '__all__'
    template_name = 'bookings/update.html'
    success_url = reverse_lazy('apps.bookings:list')  
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"¡La reserva fue actualizada correctamente!")
        return response 

class BookingsDeleteView(generic.DeleteView):
    model = Bookings
    success_url = reverse_lazy("bookings:listar")
    template_name = 'bookings/delete.html'  
    
class BookingsListView(generic.ListView):
    model= Bookings
    template_name = 'bookings/list.html'
    context_object_name = 'bookings'   
    

    
 
    