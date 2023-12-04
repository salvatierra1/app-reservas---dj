import pytest
from django.test import Client
from django.urls import reverse
from apps.employees.models import Employees 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db 
def test_create_employees(client):
    url = reverse('apps.employees:new')
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'name': 'juan', 'last_name': 'martinez', 'number_file': 13, 'state': True})
    assert response.status_code == 302
    assert response.url == reverse('apps.employees:list')
    assert Employees.objects.filter(name='juan', last_name='martinez', number_file=13, state=True).exists()