from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', include('apps.bookings.urls', namespace='bookings')),
    path('coordinators/', include('apps.coordinators.urls', namespace='coorinators')),
    path('customers/', include('apps.customers.urls', namespace='customers')),
    path('employes/', include('apps.employes.urls', namespace='employes')),
    path('services/', include('apps.services.urls', namespace='services')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)