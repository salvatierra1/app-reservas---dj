from django.urls import path 
from . import views  

app_name = 'apps.bookings'


urlpatterns = [
     path('create/', views.BookingsCreateView.as_view(), name ='create'),
     path('delete/', views.BookingsDeleteView.as_view(), name ='delete'),
     path('list/', views.BookingsListView.as_view(), name ='list'),
     path('update/<int:id>/', views.BookingsUpdateView.as_view(), name ='update'), 
       
]