from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.home.views import CustomLoginView, CustomLogoutView



schema_view = get_schema_view(
   openapi.Info(
      title="App de Reserva para Eventos",
      default_version='v1',
      description="Desarrollar una aplicación web que permita registrar servicios, empleados y clientes, realizar reservas y visualizar listados. Se requiere un endpoint para consultar y filtrar servicios, mostrando detalles completos mediante un ID.",
      terms_of_service="http://127.0.0.1:8000/",
      contact=openapi.Contact(email="alkemy@gmail.com"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('home/', include('apps.home.urls', namespace='home')),
    path('bookings/', include('apps.bookings.urls', namespace='bookings')),
    path('coordinators/', include('apps.coordinators.urls', namespace='coordinators')),
    path('customers/', include('apps.customers.urls', namespace='customers')),
    path('employees/', include('apps.employees.urls', namespace='employees')),
    path('services/', include('apps.services.urls', namespace='services')),
    #Api
    path('api/', include('apps.api_events.urls')),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)