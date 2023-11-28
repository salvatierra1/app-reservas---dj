from django.urls import path 
from . import views  

app_name = 'apps.customers'


urlpatterns = [
     path('new/', views.CustomersCreateView.as_view(), name ='new'),
     path('update/<int:id>/', views.CustomersUpdateView.as_view(), name ='update'),
     path('list/', views.CustomersListView.as_view(), name ='list'),
]