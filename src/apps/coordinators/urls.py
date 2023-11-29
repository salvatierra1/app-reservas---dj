from django.urls import path 
from . import views  
app_name = 'apps.coordinators'


urlpatterns = [
     path('new/', views.CoordinatorsCreateView.as_view(), name ='new'),
     path('update/<int:pk>/', views.CoordinatorsUpdateView.as_view(), name='update'),
     path('list/', views.CoordinatorsListView.as_view(), name ='list'),
     path('activate/<int:pk>/', views.CoordinatorsActivateView.as_view(), name='activate'),
]