from django.urls import path 
from . import views  

app_name = 'apps.coordinators'


urlpatterns = [

     path('create/', views.CoordinatorsCreateView.as_view(), name ='create'),
]