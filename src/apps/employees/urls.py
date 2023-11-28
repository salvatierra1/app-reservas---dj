from django.urls import path 
from . import views  

app_name = 'apps.employees'

urlpatterns = [
     path('new/', views.EmployeesCreateView.as_view(), name ='new'),
     path('update/<int:id>/', views.EmployeesUpdateView.as_view(), name ='update'),
     path('list/', views.EmployeesListView.as_view(), name ='list'),
]