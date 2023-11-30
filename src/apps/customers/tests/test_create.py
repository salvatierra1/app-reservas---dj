import pytest
from django.test import Client
from django.urls import reverse
from apps.customers.models import Customers 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db 
def test_creacion_customer(client):
    url = reverse('apps.customers:new')
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'name': 'Victor', 'last_name': 'Salvatierra', 'state': True})
    assert response.status_code == 302
    assert response.url == reverse('apps.customers:list')
    assert Customers.objects.filter(name='Victor', last_name='Salvatierra', state=True).exists()

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
    
@pytest.mark.django_db
def test_list_customer(client):
    Customers.objects.create(name='Fernando', last_name='Perez', state=True)
    Customers.objects.create(name='Rodrigo', last_name='Gomez', state=False)
    url = reverse('apps.customers:list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'customers' in response.context
    clientes_en_contexto = response.context['customers']
    assert clientes_en_contexto.count() == 2 
    assert 'Fernando' in response.content.decode()
    assert 'Perez' in response.content.decode()
    assert 'Rodrigo' in response.content.decode()
    assert 'Gomez' in response.content.decode()