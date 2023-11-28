from django.contrib import admin
from .models import Coordinators


#admin.site.register(Bookings)
# Register your models here.

@admin.register(Coordinators)
class CordinatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'dni', 'registration_date', 'state']
    list_filter = ['name', 'last_name', 'dni', 'registration_date', 'state']
    search_fields = ['name', 'last_name', 'dni']
    ordering = ['dni', 'name', 'last_name']
    

# Register your models here.
