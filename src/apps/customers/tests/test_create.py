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
def test_update_customer():
    customer = Customers.objects.create(name='Victor', last_name='Salvatierra', state=True)
    customer_update = Customers.objects.get(id=customer.id)
    customer_update.name = 'Javier'
    customer_update.last_name = 'Chavarria'
    customer_update.state = False
    customer_update.save()
    customer_updated = Customers.objects.get(id=customer.id)
    assert customer_updated.name == 'Javier'
    assert customer_updated.last_name == 'Chavarria'
    assert customer_updated.state == False
    
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