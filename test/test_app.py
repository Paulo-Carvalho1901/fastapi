from http import HTTPStatus

from fastapi.testclient import TestClient

from app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (o SUT)
    - A: Asert   - Garanta que A é A
    """
    # arrange
    cliente = TestClient(app)

    # act
    response = cliente.get('/')

    # Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/', 
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        }
    )   

    assert response.status_code == HTTPStatus.CREATED
