from sqlalchemy.orm import Session
from . import models, schemas


def createDepartamento(db: Session, departamento: schemas.DepartamentoCreate):
    db_departamento = models.Departamento(nome=departamento.nome)
    db.add(db_departamento)
    db.commit()
    db.refresh(db_departamento)
    return db_departamento

def getDepartamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Departamento).offset(skip).limit(limit).all()

def createEmpregado(db: Session, empregado: schemas.EmpregadoCreate):
    db_empregado = models.Empregado(nome_completo=empregado.nome_completo, id_departamento=empregado.id_departamento)
    db.add(db_empregado)
    db.commit()
    db.refresh(db_empregado)
    return db_empregado

def getEmpregado(db: Session, empregado_id: int):
    empregado = db.query(models.Empregado).filter(models.Empregado.id == empregado_id).first()
    empregado.tem_dependentes = bool(empregado.dependentes)
    return empregado

def get_empregados_by_departamento(db: Session, departamento_id: int):
    empregados = db.query(models.Empregado).filter(models.Empregado.id_departamento == departamento_id).all()
    for empregado in empregados:
        empregado.tem_dependentes = bool(empregado.dependentes)
    return empregados


def createDependente(db: Session, dependente: schemas.DependenteCreate):
    db_dependente = models.Dependente(nome=dependente.nome, empregado_id=dependente.id_empregado)
    db.add(db_dependente)
    db.commit()
    db.refresh(db_dependente)
    return db_dependente

def getdependentes(db: Session, empregado_id: int):
    return db.query(models.Dependente).filter(models.Dependente.id_empregado == empregado_id).all()