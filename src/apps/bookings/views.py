from datetime import datetime, timezone
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from apps.coordinators.models import Coordinators
from apps.customers.models import Customers
from apps.employees.models import Employees
from apps.services.models import Services
from .models import Bookings
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import qrcode
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string



# Create your views here.

class BookingsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Bookings
    template_name = 'bookings/create.html'
    fields = ['date', 'customer', 'service', 'coordinators']
    context_object_name = 'bookings'
    success_url = reverse_lazy('apps.bookings:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customers.objects.filter(state=True).order_by('name')
        context['services'] = Services.objects.filter(state=True).order_by('name')
        context['coordinators'] = Coordinators.objects.filter(state=True).order_by('name')
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

        customer_email = form.instance.customer.email
        self.send_booking_confirmation_email(customer_email)
        print(response.status_code)
        print(response.headers)

        return response
    
    def send_booking_confirmation_email(self, customer_email):   
        booking = self.object  # Obtener la instancia de la reserva creada

        subject = '¡Confirmación de Reserva! 🎉'
        message = 'Gracias por realizar la reserva. Detalles de la reserva:\n\n'
        
        message += f'Fecha de reserva: {booking.date}\n'
        message += f'Servicio: {booking.service}\n'
        message += f'Coordinador: {booking.coordinators}\n'

        html_message = render_to_string('email/booking_confirmation_email.html', {'booking': booking})

        send_mail(
            subject,
            message,
            'victorsalvatierra230@gmail.com',
            [customer_email],
            fail_silently=False,
            html_message=html_message,
        )
       


   
   
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

class BookingsListFilterView(LoginRequiredMixin, generic.ListView):
    model = Bookings
    template_name = 'bookings/list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        queryset = Bookings.objects.all()
        search = self.request.GET.get('search')

        if search:
            queryset = Bookings.objects.filter(
                Q(customer__name__icontains=search, customer__state=True) |
                Q(customer__last_name__iexact=search, customer__state=True)
            ).distinct()

        return queryset

class BookingsDetailView(generic.DetailView):
    model= Bookings
    template_name = 'bookings/detail.html'
    context_object_name = 'booking' 

def qr_code(request, pk):
    booking = get_object_or_404(Bookings, pk=pk)
    data = f"http://127.0.0.1:8000/bookings/detail/{pk}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1.5,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response