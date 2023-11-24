from django.shortcuts import render
from .models import Bookings
from django.views import generic
# Create your views here.



class BookingsCreateView(generic.CreateView):
    model= Bookings
    fields= '__all__'
    template_name = 'bookings/create.html'