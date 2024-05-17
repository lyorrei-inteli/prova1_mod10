# API Assíncrona

Desenvolvido por Lyorrei Shono Quintão

## Introdução

Este projeto é uma API simples desenvolvida para a prova 1 do módulo 10. Implementa uma API RESTful assíncrona usando Flask em Python e inclui um CRUD de pedidos.

## Requisitos

- Python
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- SQLite

## Configuração e Instalação

Antes de tudo, clone o repositório:
```bash
git clone git@github.com:lyorrei-inteli/prova1_mod10.git
cd prova1_mod10
```

Depois, navegue até a root do repositório e siga os passos a seguir dependendo se deseja rodar localmente ou via Docker:

### Localmente
1. Crie o ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicialize o banco de dados:
   ```bash
   python3 main.py create_db
   ```

4. Execute a aplicação:
   ```bash
   python3 main.py
   ```

   A aplicação estará disponível em `http://127.0.0.1:5000/`.

### Docker
1. Rode o container docker:
   ```bash
   docker compose up
   ```

A aplicação estará disponível em `http://127.0.0.1:5000/`.


## Rotas da API

- `GET, POST, PUT, DELETE /pedidos`: Rotas para gerenciamento de pedidos.
  - `GET /pedidos`: Lista todos os pedidos.
  - `POST /novo`: Cria um novo pedido.
  - `GET /pedidos/{id}`: Obtém um pedido específico.
  - `PUT /pedidos/{id}`: Atualiza um pedido específico.
  - `DELETE /pedidos/{id}`: Deleta um pedido específico.


## Estrutura do Projeto

- `main.py`: O arquivo principal da aplicação Flask.
- `database/`: Configuração do banco de dados e modelos.
- `routes/`: Rotas da API.
- `static/`: Arquivos estáticos, como o arquivo YAML do Insomnia.
- `instance/`: Arquivo project.db para o SQLite.

## Insomnia

- O arquivo YAML do Insomnia está localizado dentro da pasta `static`.
Você pode utilizar o arquivo `static/Insomnia.yaml` para importar as requisições no Insomnia e testá-las.

## Vídeo de demonstração
https://youtu.be/IQ2VZNZnKlk