from django.shortcuts import render
from .models import Customers
from django.views import generic

# Create your views here.
class CustomersCreateView(generic.CreateView):
    model= Customers
    fields= '__all__'
    template_name = 'customers/create.html'