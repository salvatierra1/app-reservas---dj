from django.shortcuts import get_object_or_404, redirect, render
from .models import Coordinators
from django.views import View, generic
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class CoordinatorsCreateView(generic.CreateView):
    model= Coordinators
    fields= '__all__'
    template_name = 'coordinators/create.html'
    success_url = reverse_lazy('apps.coordinators:list')
    
    def form_valid(self, form):
        dni = form.cleaned_data['dni']
        if Coordinators.objects.filter(dni=dni).exists():
            messages.error(self.request, f"Ya existe un coordinador con el número de dni '{dni}'.")
            return self.form_invalid(form)
        response = super().form_valid(form)
        messages.success(self.request, f"¡El coordinador '{self.object.name}' fue creado correctamente!")
        return response
    
class CoordinatorsUpdateView(generic.UpdateView):
    model = Coordinators
    fields= '__all__'
    template_name = 'coordinators/update.html'
    success_url = reverse_lazy('apps.coordinators:list')
    
    def form_valid(self, form):
        dni = form.cleaned_data['dni']
        if Coordinators.objects.filter(dni=dni).exists():
            messages.error(self.request, f"Ya existe un coordinador con el número de dni '{dni}'.")
            return self.form_invalid(form)
        response = super().form_valid(form)
        messages.success(self.request, f"¡El coordinador '{self.object.name}' fue actualizado correctamente!")
        return response
    
class CoordinatorsListView(generic.ListView):
    model= Coordinators
    template_name = 'coordinators/list.html'
    context_object_name = 'coordinators'
    
class CoordinatorsActivateView(View):
    success_url = reverse_lazy('apps.coordinators:list')
    
    def post(self, request, pk, *args, **kwargs):
        coordinator = get_object_or_404(Coordinators, pk=pk)
        coordinator.state = True
        coordinator.save()
        messages.success(self.request, f"¡El coordinador fue activado correctamente!")
        return redirect(self.success_url)

class CoordinatorsDisabledView(View):
    success_url = reverse_lazy('apps.coordinators:list')
    
    def post(self, request, pk, *args, **kwargs):
        coordinator = get_object_or_404(Coordinators, pk=pk)
        coordinator.state = False
        coordinator.save()
        messages.success(self.request, f"¡El coordinador fue desactivado correctamente!")
        return redirect(self.success_url)