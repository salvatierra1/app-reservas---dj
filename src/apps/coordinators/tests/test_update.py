import pytest
from django.test import Client
from django.urls import reverse
from apps.coordinators.models import Coordinators 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db 
def test_update_coordinators(client):
    coordinator = Coordinators.objects.create(name= 'Daniel', last_name= 'Perez', dni= 23578898, state= True)
    url = reverse('apps.coordinators:update', kwargs={'pk': coordinator.pk})
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'name': 'Fernando', 'last_name': 'Lopez', 'dni': 45234567, 'state': False})
    assert response.status_code == 302
    assert response.url == reverse('apps.coordinators:list')
    coordinator.refresh_from_db()
    assert coordinator.name == 'Fernando'
    assert coordinator.last_name == 'Lopez'
    assert coordinator.dni == 45234567
    assert coordinator.state == False
    