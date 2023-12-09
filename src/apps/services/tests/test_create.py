import pytest
from django.test import Client
from django.urls import reverse
from apps.services.models import Services 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db 
def test_create_services(client):
    url = reverse('apps.services:new')
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'name': 'Salon de 15 años', 'description': 'Juegos, iluminación', 'price': 130, 'state': True})
    assert response.status_code == 302
    assert response.url == reverse('apps.services:list')
    assert Services.objects.filter(name = 'Salon de 15 años', description ='Juegos, iluminación', price = 130, state = True).exists()
    
      