import pytest
from django.test import Client
from django.urls import reverse
from apps.employees.models import Employees 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db 
def test_update_employees(client):
    employee = Employees.objects.create(name= 'diego', last_name= 'torres', number_file= 8, state= True)
    url = reverse('apps.employees:update', kwargs={'pk': employee.pk}) 
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'name': 'facundo', 'last_name': 'castillo', 'number_file': 6, 'state': False})
    assert response.status_code == 302
    assert response.url == reverse('apps.employees:list')
    employee.refresh_from_db()
    assert employee.name == 'facundo'
    assert employee.last_name == 'castillo'
    assert employee.number_file == 6
    assert employee.state == False
