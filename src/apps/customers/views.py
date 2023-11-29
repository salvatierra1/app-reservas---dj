from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Customers
from django.views import View, generic

# Create your views here.
class CustomersCreateView(generic.CreateView):
    model= Customers
    fields= '__all__'
    template_name = 'customers/create.html'
    success_message = "¡El cliente '%(name)s' fue creado correctamente!"
    success_url = reverse_lazy('apps.customers:list')

class CustomersUpdateView(generic.UpdateView):
    model= Customers
    fields= '__all__'
    template_name = 'customers/update.html'
    success_message = "¡El cliente '%(name)s' fue actualizado correctamente!"
    success_url = reverse_lazy('apps.customers:list')
    
class CustomersListView(generic.ListView):
    model= Customers
    template_name = 'customers/list.html'
    context_object_name = 'customers'
    
class CustomersActivateView(View):
    success_url = reverse_lazy('apps.customers:list')

    def post(self, request, pk, *args, **kwargs):
        customers = get_object_or_404(customers, pk=pk)
        customers.state = True
        customers.save()
        return redirect(self.success_url)
