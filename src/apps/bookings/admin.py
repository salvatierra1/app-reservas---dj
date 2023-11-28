from django.contrib import admin
from .models import Bookings


#admin.site.register(Bookings)
# Register your models here.

@admin.register(Bookings)
class BookingAdmin(admin.ModelAdmin):
    list_display=['date','customer', 'service', 'employee', 'coordinators']
    list_filter = ['date','customer', 'service', 'employee', 'coordinators']
    list_search = ['date','customer', 'service', 'employee', 'coordinators']
    ordering = ['date', 'customer']