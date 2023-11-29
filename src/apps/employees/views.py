from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Employees
from django.views import View, generic

# Create your views here.

class EmployeesCreateView(generic.CreateView):
    model= Employees
    fields= '__all__'
    template_name = 'employees/create.html'
    success_message = "¡El empleado '%(name)s' fue creado correctamente!"
    success_url = reverse_lazy('apps.employees:list')

class EmployeesUpdateView(generic.UpdateView):
    model= Employees
    fields= '__all__'
    template_name = 'employees/update.html'
    success_message = "¡El empleado '%(name)s' fue actualizado correctamente!"
    success_url = reverse_lazy('apps.employees:list')
    
class EmployeesListView(generic.ListView):
    model= Employees
    template_name = 'employees/list.html'
    context_object_name = 'employees'
