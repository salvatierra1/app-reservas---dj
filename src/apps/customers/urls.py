from django.urls import path 
from . import views  

app_name = 'apps.customers'


urlpatterns = [
     path('new/', views.CustomersCreateView.as_view(), name ='new'),
     path('update/<int:pk>/', views.CustomersUpdateView.as_view(), name ='update'),
     path('list/', views.CustomersListView.as_view(), name ='list'),
     path('activate/<int:pk>/', views.CustomersActivateView.as_view(), name='activate'),
     path('disabled/<int:pk>/', views.CustomersDisabledView.as_view(), name='disabled'),
     path('filter/', views.CustomersListFilterView.as_view(), name ='filter'),
]