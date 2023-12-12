from datetime import datetime, timezone
from django.shortcuts import render
from apps.coordinators.models import Coordinators
from apps.customers.models import Customers
from apps.employees.models import Employees
from apps.services.models import Services
from .models import Bookings
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BookingsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Bookings
    template_name = 'bookings/create.html'
    fields = ['date', 'customer', 'service', 'coordinators']
    context_object_name = 'bookings'
    success_url = reverse_lazy('apps.bookings:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customers.objects.all()
        context['services'] = Services.objects.all()
        context['coordinators'] = Coordinators.objects.all()
        return context

    def form_valid(self, form):
        date = form.cleaned_data['date']
        current_datetime = datetime.now(timezone.utc)
        current_date = current_datetime.date()
        input_date = date.date()
        if input_date < current_date:
            messages.error(self.request, "¡La fecha no puede ser menor a la actual!")
            return self.form_invalid(form)

        employee = Employees.objects.get(user=self.request.user)

        form.instance.employee = employee

        response = super().form_valid(form)
        messages.success(self.request, "¡La reserva fue creada correctamente!")
        return response
       
class BookingsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Bookings
    template_name = 'bookings/update.html'
    fields = ['date', 'customer', 'service', 'coordinators']
    context_object_name = 'bookings'
    success_url = reverse_lazy('apps.bookings:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['customers'] = Customers.objects.all()
        context['services'] = Services.objects.all()
        context['coordinators'] = Coordinators.objects.all()
        return context
    
    def form_valid(self, form):
        employee = Employees.objects.get(user=self.request.user)
        form.instance.employee = employee
        response = super().form_valid(form)
        messages.success(self.request, f"¡La reserva fue actualizada correctamente!")
        return response 

class BookingsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Bookings
    template_name = 'bookings/delete.html'
    
    def get_success_url(self):
        messages.success(self.request, "¡La reserva fue eliminada correctamente!")
        return reverse("apps.bookings:list")
    
class BookingsListView(LoginRequiredMixin, generic.ListView):
    model= Bookings
    template_name = 'bookings/list.html'
    context_object_name = 'bookings'   
    

    
 
    