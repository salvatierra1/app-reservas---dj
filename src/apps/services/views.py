from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Services
from django.views import View, generic
from django.contrib import messages

# Create your views here.
class ServicesCreateView(generic.CreateView):
    model= Services
    fields= '__all__'
    template_name = 'services/create.html'
    success_url = reverse_lazy('apps.services:list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"¡El servicio '{self.object.name}' fue creado correctamente!")
        return response

class ServicesUpdateView(generic.UpdateView):
    model= Services
    fields= '__all__'
    template_name = 'services/update.html'
    success_url = reverse_lazy('apps.services:list')   

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"¡El servicio '{self.object.name}' fue actualizado correctamente!")
        return response

class ServicesListView(generic.ListView):
    model= Services
    template_name = 'services/list.html'
    context_object_name = 'services'

class ServicesActivateView(View):
    success_url = reverse_lazy('apps.services:list')

    def post(self, request, pk, *args, **kwargs):
        service = get_object_or_404(Services, pk=pk)
        service.state = True
        service.save()
        messages.success(self.request, f"¡El servicio fue activado correctamente!")
        return redirect(self.success_url)

class ServicesDisabledView(View):
    success_url = reverse_lazy('apps.services:list')
    
    def post(self, request, pk, *args, **kwargs):
        service = get_object_or_404(Services, pk=pk)
        service.state = False
        service.save()
        messages.success(self.request, f"¡El servicio fue desactivado correctamente!")
        return redirect(self.success_url)