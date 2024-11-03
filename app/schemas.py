from typing import Optional
from pydantic import BaseModel

class DepartamentoBase(BaseModel):
    nome: str

class DepartamentoCreate(DepartamentoBase):
    pass

class Departamento(DepartamentoBase):
    id: int
    class Config:
        orm_mode = True

class EmpregadoBase(BaseModel):
    nome_completo: str
    id_departamento: int

class EmpregadoCreate(EmpregadoBase):
    pass

class Empregado(EmpregadoBase):
    id: int
    tem_dependentes: Optional[bool]= None
    class Config:
        orm_mode = True

class DependenteBase(BaseModel):
    nome: str
    id_empregado: int

class DependenteCreate(DependenteBase):
    pass

class Dependente(DependenteBase):
    id: int
    class Config:
        orm_mode = True
