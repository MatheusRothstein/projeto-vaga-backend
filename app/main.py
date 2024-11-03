from fastapi import FastAPI
from .database import engine, Base
from .routers import departamento, empregados

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    departamento.router, prefix='/departamento', tags=['Departamentos']
)
app.include_router(
    empregados.router, prefix='/empregados', tags=['Empregados']
)
