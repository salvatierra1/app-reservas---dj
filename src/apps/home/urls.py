# En tu archivo apps/home/urls.py
from django.urls import path
from .views import IndexView

app_name = 'apps.home'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
