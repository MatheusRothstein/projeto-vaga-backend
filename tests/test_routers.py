import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


@pytest.fixture()
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client(db):
    def get_session_override():
        return db

    with TestClient(app) as client:
        app.dependency_overrides[get_db] = get_session_override
        yield client


def test_criar_departamento(client, db):
    response = client.post('/departamento/', json={'nome': 'TI'})
    assert response.status_code == 201
    assert response.json()['nome'] == 'TI'


def test_listar_departamento(client, db):
    client.post('/departamento/', json={'nome': 'RH'})

    response = client.get('/departamento')
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]['nome'] == 'RH'
