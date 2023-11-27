from django.shortcuts import render
from .models import Employees
from django.views import generic

# Create your views here.

class EmployeesCreateView(generic.CreateView):
    model= Employees
    fields= '__all__'
    template_name = 'employees/create.html'