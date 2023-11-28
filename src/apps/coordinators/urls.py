from django.urls import path 
from . import views  

app_name = 'apps.coordinators'


urlpatterns = [
     path('new/', views.CoordinatorsCreateView.as_view(), name ='new'),
     path('update/<int:id>/', views.CoordinatorsUpdateView.as_view(), name ='update'), 
     path('list/', views.CoordinatorsListView.as_view(), name ='list'),
]