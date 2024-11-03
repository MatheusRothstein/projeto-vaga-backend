from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Departamento])
def read_departamento(db: Session = Depends(get_db)):
    return crud.getDepartamentos(db)

@router.post("/", response_model=schemas.Departamento)
def create_deparamento(departamento: schemas.DepartamentoCreate, db: Session = Depends(get_db)):
    return crud.createDepartamento(db=db, departamento=departamento)
