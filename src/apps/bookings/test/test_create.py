import pytest
from django.test import Client
from django.urls import reverse
from apps.bookings.models import Bookings
from apps.services.models import Services
from apps.employees.models import Employees 
from apps.customers.models import Customers
from apps.coordinators.models import Coordinators
    
    
    
    
@pytest.fixture
def customer():
    return Customers.objects.create(name='Victor', last_name='Salvatierra', state=True)   
    
@pytest.fixture
def service():
    return Services.objects.create(name='casamiento',description='catering y sonido', price='30000', state= True)
    
@pytest.fixture
def employee():
    return Employees.objects.create(name='javier',last_name='chavarria',number_file='34328318', state=True)
    
@pytest.fixture
def coordinator():
    return Coordinators.objects.create(name='matias',last_name='quiroga',dni='39313147',registration_date='19/06/2024 00:00:00',state=True)
        
        
@pytest.fixture
def client():
    return Client()    
    
@pytest.mark.django_db
def test_create_bookings(client):
    url = reverse('apps.bookings:new')
    response = client.get(url)
    assert response.status_code == 200
    response = client.post(url, {'date':'20/06/2024 00:00:00', 'customer':customer, 'service':service, 'employee':employee, 'coordinator':coordinator})
    assert response.status_code == 302
    assert response.url == reverse('apps.bookings:list')
    assert Services.objects.filter(date = '20/06/2024 00:00:00', customer='Victor', service='casamiento', employee='javier', coordinator='matias').exists()
