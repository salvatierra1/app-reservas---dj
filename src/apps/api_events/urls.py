from django.urls import path
from . import views  

app_name = 'apps.api_events'

urlpatterns = [
    path('coordinators/', views.CoordinatorsListAPIView.as_view(), name='list'),
    path('coordinators/<int:pk>', views.CoordinatorsRetrieveAPIView.as_view(), name='detail'),
    path('services/', views.ServicesListAPIView.as_view(), name='list'),
    path('services/<int:pk>', views.ServicesRetrieveAPIView.as_view(), name='detail'),
    path('employees/', views.EmployeesListAPIView.as_view(), name='list'),
    path('employees/<int:pk>', views.EmployeesRetrieveAPIView.as_view(), name='detail'),
]
