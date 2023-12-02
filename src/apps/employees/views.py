from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Employees
from django.views import generic
from django.contrib import messages

# Create your views here.
class EmployeesCreateView(generic.CreateView):
    model= Employees
    fields= '__all__'
    template_name = 'employees/create.html'
    success_url = reverse_lazy('apps.employees:list')
    
    def form_valid(self, form):
        number_file = form.cleaned_data['number_file']
        if Employees.objects.filter(number_file=number_file).exists():
            messages.error(self.request, f"Ya existe un empleado con el número de legajo '{number_file}'.")
            return self.form_invalid(form)
        response = super().form_valid(form)
        messages.success(self.request, f"¡El empleado '{self.object.name}' fue creado correctamente!")
        return response

class EmployeesUpdateView(generic.UpdateView):
    model= Employees
    fields= '__all__'
    template_name = 'employees/update.html'
    success_url = reverse_lazy('apps.employees:list')
    
    def form_valid(self, form):
        number_file = form.cleaned_data['number_file']
        if Employees.objects.filter(number_file=number_file).exists():
            messages.error(self.request, f"Ya existe un empleado con el número de legajo '{number_file}'.")
            return self.form_invalid(form)
        response = super().form_valid(form)
        messages.success(self.request, f"¡El empleado '{self.object.name}' fue actualizado correctamente!")
        return response
    
class EmployeesListView(generic.ListView):
    model= Employees
    template_name = 'employees/list.html'
    context_object_name = 'employees'
