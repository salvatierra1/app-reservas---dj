import pytest
from django.test import Client
from django.urls import reverse
from apps.services.models import Services 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db 
def test_update_services(client):
    service = Services.objects.create(name= 'Salon de 15', description= 'iluminacion', price= 8, state= True)
    url = reverse('apps.services:update', kwargs={'pk': service.pk}) 
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'name': 'Salon de casamiento', 'description': 'Juegos, iluminacion', 'price': 600, 'state': False})
    assert response.status_code == 302
    assert response.url == reverse('apps.services:list')
    service.refresh_from_db()
    assert service.name == 'Salon de casamiento'
    assert service.description == 'Juegos, iluminacion'
    assert service.price == 600
    assert service.state == False
