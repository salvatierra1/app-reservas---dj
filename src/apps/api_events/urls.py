from django.urls import path
from . import views  

app_name = 'apps.api_events'

urlpatterns = [
    path('coordinators/', views.CoordinatorsListAPIView.as_view(), name='list'),
    path('coordinators/<int:pk>', views.CoordinatorsRetrieveAPIView.as_view(), name='detail'),
]
