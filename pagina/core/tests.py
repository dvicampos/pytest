from django.test import TestCase
import pytest
from django.urls import reverse

# Create your tests here.

@pytest.mark.django_db
def test_home_view(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200
    # assert b"¡Hola, mundo!" in response.content
    assert "¡Hola, mundo!" in response.content.decode()

@pytest.mark.django_db
def test_greet_view(client):
    response = client.get(reverse('greet', args=['juan']))
    assert response.status_code == 200
    assert b"Hola, Juan!" in response.content

def test_greet_view_invalid_name(client):
    response = client.get(reverse('greet', args=['123']))
    assert response.status_code == 400
    assert "¡Hola, mundo!" in response.content.decode()

def test_home_template(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert "<h1>¡Hola, mundo!</h1>" in response.content.decode()

