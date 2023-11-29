from django.urls import path 
from . import views  

app_name = 'apps.bookings'


urlpatterns = [
     path('create/', views.BookingsCreateView.as_view(), name ='create'),
     path('update/<int:pk>/', views.BookingsUpdateView.as_view(), name ='update'), 
     path('delete/<int:pk>/', views.BookingsDeleteView.as_view(), name ='delete'),
     path('list/', views.BookingsListView.as_view(), name ='list'),    
]