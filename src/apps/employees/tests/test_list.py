import pytest
from django.test import Client
from django.urls import reverse
from apps.employees.models import Employees 

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def client():
    return Client()
  
@pytest.mark.django_db
def test_list_employees(client):
    Employees.objects.create(name='fernando', last_name='quintero', number_file=4, state=True)
    Employees.objects.create(name='pablo', last_name='ramos', number_file=5, state=False)
    url = reverse('apps.employees:list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'employees' in response.context
    employees_en_contexto = response.context['employees']
    assert employees_en_contexto.count() == 2 
    assert 'fernando' in response.content.decode()
    assert 'quintero' in response.content.decode()
    assert '4' in response.content.decode()
    assert 'pablo' in response.content.decode()
    assert 'ramos' in response.content.decode()
    assert '5' in response.content.decode()