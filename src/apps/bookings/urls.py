from django.urls import path 
from . import views  

app_name = 'apps.bookings'


urlpatterns = [
     path('create/', views.BookingsCreateView.as_view(), name ='create'),
]