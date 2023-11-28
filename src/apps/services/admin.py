from django.contrib import admin
from .models import Services
# Register your models here.
#admin.site.register(Beneficiario)

#metodo para filtrado de informacion en el panel de administrador
@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price','state']
    list_filter = ['name', 'description', 'price','state']
    search_fields = ['name', 'description', 'price','state']
    ordering = ['name', 'description', 'price','state']