from django.urls import path 
from . import views  

app_name = 'apps.bookings'

urlpatterns = [
     path('new/', views.BookingsCreateView.as_view(), name ='new'),
     path('update/<int:pk>/', views.BookingsUpdateView.as_view(), name ='update'), 
     path('delete/<int:pk>/', views.BookingsDeleteView.as_view(), name ='delete'),
     path('list/', views.BookingsListView.as_view(), name ='list'),
     path('filter/', views.BookingsListFilterView.as_view(), name ='filter'),
     path('detail/<int:pk>', views.BookingsDetailView.as_view(), name ='detail'),
     path('qr_code/<int:pk>', views.qr_code, name='qr_code'),   
]