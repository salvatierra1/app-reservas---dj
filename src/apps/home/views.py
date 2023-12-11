from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from apps.bookings.models import Bookings
from apps.customers.models import Customers
from apps.employees.models import Employees
from apps.coordinators.models import Coordinators
from apps.services.models import Services
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html' 
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            bookings = Bookings.objects.all()
            total_bookings = bookings.count()
            context['total_bookings'] = total_bookings
            
            customers = Customers.objects.all()
            total_customers = customers.count()
            context['total_customers'] = total_customers
            
            services = Services.objects.all()
            total_services = services.count()
            context['total_services'] = total_services
            
            coordinators = Coordinators.objects.all()
            total_coordinators = coordinators.count()
            context['total_coordinators'] = total_coordinators
            
            employees = Employees.objects.all()
            total_employees = employees.count()
            context['total_employees'] = total_employees
            return context