from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from apps.bookings.models import Bookings

class IndexView(TemplateView):
    template_name = 'home/index.html' 
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            bookings = Bookings.objects.all()
            total_bookings = bookings.count()
            context['total_bookings'] = total_bookings
            return context