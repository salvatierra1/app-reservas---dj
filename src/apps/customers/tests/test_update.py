import pytest
from django.test import Client
from django.urls import reverse
from apps.customers.models import Customers 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db 
def test_update_customer(client):
    customer = Customers.objects.create(name='Antonio', last_name='Gomez', state=True)
    url = reverse('apps.customers:update', kwargs={'pk': customer.pk})
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'name': 'Fernando', 'last_name': 'Lopez', 'state': False})
    assert response.status_code == 302
    assert response.url == reverse('apps.customers:list')
    customer.refresh_from_db()
    assert customer.name == 'Fernando'
    assert customer.last_name == 'Lopez'
    assert customer.state == False
