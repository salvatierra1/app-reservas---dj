from django.urls import path 
from . import views  

app_name = 'apps.customers'


urlpatterns = [

     path('create/', views.CustomersCreateView.as_view(), name ='create'),
]