import pytest
from django.test import Client
from django.urls import reverse
from apps.coordinators.models import Coordinators 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db 
def test_create_coordinators(client):
    url = reverse('apps.coordinators:new')
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'name': 'Daniel', 'last_name': 'Perez', 'dni': 23578898, 'state': True})
    assert response.status_code == 302
    assert response.url == reverse('apps.coordinators:list')
    assert Coordinators.objects.filter(name='Daniel', last_name='Perez', dni=23578898, state=True).exists()

