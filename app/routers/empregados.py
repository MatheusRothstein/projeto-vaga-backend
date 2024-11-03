from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from http import HTTPStatus
from .. import crud, schemas
from ..database import get_db

router = APIRouter()


@router.get('/{id_departamento}', response_model=List[schemas.Empregado])
def read_empregado(id_departamento: int, db: Session = Depends(get_db)):
    empregados = crud.get_empregados_by_departamento(db, id_departamento)
    for empregado in empregados:
        empregado.tem_dependentes = len(empregado.dependentes) > 0
    return empregados


@router.post(
    '/', response_model=schemas.Empregado, status_code=HTTPStatus.CREATED
)
def create_empregado(
    empregado: schemas.EmpregadoCreate, db: Session = Depends(get_db)
):
    return crud.createEmpregado(db=db, empregado=empregado)
