import json
import pytest
from django.urls import reverse
from django.test import Client
from apps.coordinators.models import Coordinators 


@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db
def test_list_coordinators(client):
    
    Coordinators.objects.create(name='Julio', last_name='Perez', dni=34098765, state=True)
    Coordinators.objects.create(name='Rodrigo', last_name='Gomez', dni=32098765, state=False)

    url = reverse('apps.api_events:list')
    response = client.get(url)

    assert response.status_code == 200

    content_type = response.headers.get('Content-Type', '')
    assert 'application/json' in content_type, "La respuesta no es de tipo JSON"

    try:
        json_data = json.loads(response.content)
        assert isinstance(json_data, list)
        assert len(json_data) == 2  

        for coordinator_data in json_data:
            assert 'id' in coordinator_data
            assert 'name' in coordinator_data
            
    except json.JSONDecodeError:
        pytest.fail("La respuesta no es JSON.")

@pytest.mark.django_db
def test_coordinator_detail(client):
    coordinator = Coordinators.objects.create(name='Victor', last_name='Salvatierra', dni=12345678, state=True)
    url = reverse('apps.api_events:detail', kwargs={'pk': coordinator.pk})  
    response = client.get(url)
    assert response.status_code == 200
    try:
        json_data = json.loads(response.content)
        assert 'name' in json_data 
        assert json_data['name'] == 'Victor'
        assert json_data['last_name'] == 'Salvatierra'
        assert json_data['dni'] == 12345678
        assert json_data['state'] == True
    except json.JSONDecodeError:
        pytest.fail("La respuesta no es JSON.")