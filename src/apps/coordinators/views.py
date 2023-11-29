from django.shortcuts import get_object_or_404, redirect, render
from .models import Coordinators
from django.views import View, generic
from django.urls import reverse_lazy

# Create your views here.


class CoordinatorsCreateView(generic.CreateView):
    model= Coordinators
    fields= '__all__'
    template_name = 'coordinators/create.html'
    success_message = "¡El coordinador '%(name)s' fue creado correctamente!"
    success_url = reverse_lazy('apps.coordinators:list')
    
class CoordinatorsUpdateView(generic.UpdateView):
    model = Coordinators
    fields= '__all__'
    template_name = 'coordinators/update.html'
    success_message = "¡El coordinador '%(name)s' fue actualizado correctamente!"
    success_url = reverse_lazy('apps.coordinators:list')
    
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
        return redirect(self.success_url)

class CoordinatorsDisabledView(View):
    success_url = reverse_lazy('apps.coordinators:list')
    
    def post(self, request, pk, *args, **kwargs):
        coordinator = get_object_or_404(Coordinators, pk=pk)
        coordinator.state = False
        coordinator.save()
        return redirect(self.success_url)