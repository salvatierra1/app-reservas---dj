from django.urls import path 
from . import views  

app_name = 'apps.services'


urlpatterns = [

     path('create/', views.ServicesCreateView.as_view(), name ='create'),
]