from django.urls import path 
from . import views  

app_name = 'apps.services'


urlpatterns = [
     path('new/', views.ServicesCreateView.as_view(), name ='new'),
     path('list/', views.ServicesListView.as_view(), name ='list'),
]