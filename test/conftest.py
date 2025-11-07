import pytest
from fastapi.testclient import TestClient

from app import app


# Teste reutilizavel
@pytest.fixture
def client():
    return TestClient(app)