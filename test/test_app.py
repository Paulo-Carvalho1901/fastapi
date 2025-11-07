from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app

import pytest

# Teste reutilizavel
@pytest.fixture
def client():
    return TestClient(app)

def test_root_deve_retornar_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (o SUT)
    - A: Asert   - Garanta que A é A
    """

    # act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/', 
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        }
    )   

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }
