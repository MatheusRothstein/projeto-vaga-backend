import pytest
from app.crud import (
    createDepartamento,
    createEmpregado,
    getDepartamentos,
    getEmpregado,
    get_empregados_by_departamento,
)
from app.database import Base, get_db
from app.models import Departamento, Empregado
from app.schemas import DepartamentoCreate, EmpregadoCreate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


@pytest.fixture(scope='function')
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_criar_departamento(db):
    departamento_data = DepartamentoCreate(nome='TI')
    departamento = createDepartamento(db=db, departamento=departamento_data)
    assert departamento.nome == 'TI'


def test_listar_departamentos(db):
    createDepartamento(db=db, departamento=DepartamentoCreate(nome='TI'))
    departamentos = getDepartamentos(db=db)
    assert len(departamentos) == 1
    assert departamentos[0].nome == 'TI'


def test_criar_empregado(db):
    departamento = createDepartamento(
        db=db, departamento=DepartamentoCreate(nome='TI')
    )
    empregado_data = EmpregadoCreate(
        nome_completo='Ichigo Kurosaki', id_departamento=departamento.id
    )
    empregado = createEmpregado(db=db, empregado=empregado_data)
    assert empregado.nome_completo == 'Ichigo Kurosaki'
    assert empregado.id_departamento == departamento.id


def test_listar_empregado_por_departamento(db):
    departamento = createDepartamento(
        db=db, departamento=DepartamentoCreate(nome='TI')
    )
    createEmpregado(
        db=db,
        empregado=EmpregadoCreate(
            nome_completo='Ichigo', id_departamento=departamento.id
        ),
    )

    empregados = get_empregados_by_departamento(
        db=db, departamento_id=departamento.id
    )
    assert len(empregados) == 1
    assert empregados[0].nome_completo == 'Ichigo'
