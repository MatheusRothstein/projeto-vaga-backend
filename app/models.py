from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Departamento(Base):
    __tablename__ = 'departamentos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)

    # Relacionamento com Empregado (nome 'empregados' precisa corresponder em Empregado)
    empregados = relationship('Empregado', back_populates='departamento')


class Empregado(Base):
    __tablename__ = 'empregados'
    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String, index=True)
    id_departamento = Column(Integer, ForeignKey('departamentos.id'))

    # Relacionamento com Departamento (nome 'departamento' precisa corresponder em Departamento)
    departamento = relationship('Departamento', back_populates='empregados')

    # Relacionamento com Dependente (nome 'dependentes' precisa corresponder em Dependente)
    dependentes = relationship('Dependente', back_populates='empregado')


class Dependente(Base):
    __tablename__ = 'dependentes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    id_empregado = Column(Integer, ForeignKey('empregados.id'))

    # Relacionamento com Empregado (nome 'empregado' precisa corresponder em Empregado)
    empregado = relationship('Empregado', back_populates='dependentes')
