import pytest
from django.test import Client
from django.urls import reverse
from apps.customers.models import Customers 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db 
def test_create_customer(client):
    url = reverse('apps.customers:new')
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'name': 'Victor', 'last_name': 'Salvatierra', 'state': True})
    assert response.status_code == 302
    assert response.url == reverse('apps.customers:list')
    assert Customers.objects.filter(name='Victor', last_name='Salvatierra', state=True).exists()