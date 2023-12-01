import pytest
from django.test import Client
from django.urls import reverse
from apps.customers.models import Customers 

@pytest.fixture
def client():
    return Client()
  
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