# Documentação da API ACMEVita

## Visão Geral

A API da ACMEVita permite o gerenciamento de departamentos, colaboradores e seus dependentes. O sistema foi desenvolvido utilizando o framework FastAPI e SQLAlchemy, e fornece endpoints para criar, consultar e gerenciar dados de forma eficiente.

### Estrutura do Projeto

- **app/**
  - **main.py**: Ponto de entrada da aplicação.
  - **models.py**: Definições dos modelos de dados utilizando SQLAlchemy.
  - **schemas.py**: Esquemas de validação utilizando Pydantic.
  - **crud.py**: Funções de acesso aos dados (CRUD).
  - **database.py**: Configurações de conexão com o banco de dados.
  - **routers/**
    - **departamento.py**: Roteador para endpoints de departamentos.
    - **empregados.py**: Roteador para endpoints de empregados.
  - **tests**
    - **test_crud.py**
    - **test_routers.py**

### Requisitos

- Python 3.7 ou superior
- FastAPI
- SQLAlchemy
- Pydantic
- Banco de dados (SQLite, PostgreSQL, etc.)

### Link para a documentação das rotas
http://localhost:8000/docs

## Instalando o Ambiente

1. **Clone o repositório:**

  ```bash
   git clone https://github.com/seu_usuario/acmevita.git
   cd acmevita
   ```

2. **Construindo a imagem docker:**

  ```bash
  docker-compose build
  ```

3. **Executando a aplicação**
  ```bash
  docker-compose up
  ```

4. **Rodando os testes**
  ```bash
  docker-compose exec web bash
  pytest -v
  ```