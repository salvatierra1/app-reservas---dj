from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('apps.home.urls', namespace='home')),
    path('bookings/', include('apps.bookings.urls', namespace='bookings')),
    path('coordinators/', include('apps.coordinators.urls', namespace='coordinators')),
    path('customers/', include('apps.customers.urls', namespace='customers')),
    path('employees/', include('apps.employees.urls', namespace='employees')),
    path('services/', include('apps.services.urls', namespace='services')),
    #Api
    path('api/', include('apps.api_events.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)