import pytest
from django.test import Client
from django.urls import reverse
from apps.coordinators.models import Coordinators 

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db
def test_list_coordinators(client):
    Coordinators.objects.create(name='Julio', last_name='Perez', dni=34098765, state=True)
    Coordinators.objects.create(name='Rodrigo', last_name='Gomez', dni=32098765, state=False)
    url = reverse('apps.coordinators:list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'coordinators' in response.context
    coordinators_en_contexto = response.context['coordinators']
    assert coordinators_en_contexto.count() == 2 
    assert 'Julio' in response.content.decode()
    assert 'Perez' in response.content.decode()
    assert '34098765' in response.content.decode()
    assert 'Rodrigo' in response.content.decode()
    assert 'Gomez' in response.content.decode()
    assert '32098765' in response.content.decode()