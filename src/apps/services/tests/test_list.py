import pytest
from django.test import Client
from django.urls import reverse
from apps.services.models import Services 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db
def test_list_services(client):
    Services.objects.create(name='Salon de fiesta', description='Iluminacion', price=400, state=True)
    Services.objects.create(name='Salon de juegos', description='Juegos', price=500, state=False)
    url = reverse('apps.services:list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'services' in response.context
    services_en_contexto = response.context['services']
    assert services_en_contexto.count() == 2 
    assert 'Salon de fiesta' in response.content.decode()
    assert 'Iluminacion' in response.content.decode()
    assert '400' in response.content.decode()
    assert 'Salon de juegos' in response.content.decode()
    assert 'Juegos' in response.content.decode()
    assert '500' in response.content.decode()