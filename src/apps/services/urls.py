from django.urls import path 
from . import views  

app_name = 'apps.services'

urlpatterns = [
     path('new/', views.ServicesCreateView.as_view(), name ='new'),
     path('update/<int:pk>/', views.ServicesUpdateView.as_view(), name ='update'),
     path('list/', views.ServicesListView.as_view(), name ='list'),
     path('activate/<int:pk>/', views.ServicesActivateView.as_view(), name='activate'),
     path('disabled/<int:pk>/', views.ServicesDisabledView.as_view(), name='disabled'),
     path('filter/', views.ServicesListFilterView.as_view(), name ='filter'),
]