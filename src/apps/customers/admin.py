from django.contrib import admin
from .models import Customers


#admin.site.register(Bookings)
# Register your models here.

@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','last_name','state']
    list_filter = ['name','last_name','state']
    search_fields = ['name','last_name','state']
    ordering = ['name','last_name','state']