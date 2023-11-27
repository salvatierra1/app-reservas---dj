from django.urls import path 
from . import views  

app_name = 'apps.employees'

urlpatterns = [
     path('create/', views.EmployeesCreateView.as_view(), name ='create'),
]