from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Customers
from django.views import View, generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CustomersCreateView(LoginRequiredMixin, generic.CreateView):
    model= Customers
    fields= '__all__'
    template_name = 'customers/create.html'
    success_url = reverse_lazy('apps.customers:list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"¡El cliente '{self.object.name}' fue creado correctamente!")
        return response

class CustomersUpdateView(LoginRequiredMixin, generic.UpdateView):
    model= Customers
    fields= '__all__'
    template_name = 'customers/update.html'
    success_url = reverse_lazy('apps.customers:list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"¡El cliente '{self.object.name}' fue actualizado correctamente!")
        return response
    
class CustomersListView(LoginRequiredMixin, generic.ListView):
    model= Customers
    template_name = 'customers/list.html'
    context_object_name = 'customers'
    
class CustomersActivateView(LoginRequiredMixin, View):
    success_url = reverse_lazy('apps.customers:list')

    def post(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(Customers, pk=pk)
        customer.state = True
        customer.save()
        messages.success(self.request, f"¡El cliente fue activado correctamente!")
        return redirect(self.success_url)

class CustomersDisabledView(LoginRequiredMixin, View):
    success_url = reverse_lazy('apps.customers:list')
    
    def post(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(Customers, pk=pk)
        customer.state = False
        customer.save()
        messages.success(self.request, f"¡El cliente fue desactivado correctamente!")
        return redirect(self.success_url)
    
