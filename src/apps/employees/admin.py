from django.contrib import admin
from .models import Employees
# Register your models here.


#metodo para filtrado de informacion en el panel de administrador
@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'number_file','state']
    list_filter = ['name', 'last_name', 'number_file','state']
    search_fields = ['name', 'last_name', 'number_file','state']
    ordering = ['name', 'last_name', 'number_file','state']