import pytest
from fastapi.testclient import TestClient

from app import app


# Teste reutilizavel
@pytest.fixture
def client():
    return TestClient(app)


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import table_registry


@pytest.fixure
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
