from django.urls import path 
from . import views  

app_name = 'apps.employes'

urlpatterns = [
     path('create/', views.EmployesCreateView.as_view(), name ='create'),
]