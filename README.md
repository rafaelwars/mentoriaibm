LIGAR O DOCKER

docker run --name fastapi-postgres -e POSTGRES_PASSWORD=projeto -d -p 5432:5432 postgres:alpine
-- Criamos uma imagem chamada fastapi-postgres, com a senha projeto e a porta 5432

-- depois de finalizar a criação da imagem
docker ps
verificar as imagens criadas dentro do container

--Comando para executar a imagem
docker exec -it fastapi-postgres bash

--Dentro da imagem do Postgres
psql -U postgres (Identificar a imagem)

-- Criando o banco de dados fastapi_database (arrumar o nome da tabela de databas para database)
postgres=# create database fastapi_database;
CREATE DATABASE

-- Criando o usuario projeto
postgres=# create user projeto with encrypted password 'projeto';
CREATE ROLE

-- Dando acesso total ao banco "fastapi_database" para o usuario projeto
postgres=# grant all privileges on database "fastapi_database" to projeto;
GRANT

-- Dar acesso do usuario projeto para o schema:
grant all privileges on SCHEMA public TO projeto;

-- conectando no banco "fastapi_database"
postgres=# \c fastapi_database;
You are now connected to database "fastapi_database" as user "postgres".

-- Definir a localhost para acessar remoto
fastapi_database=# psql -h localhost -p 5432 postgres

ABRIR UM NOVO TERMINAL

(Garantir que está na mesma pasta dos arquivos de python)
exemplo:

cd projetofia

-- Instalando as bibliotecas do FASTAPI, SQLAlchemy e psycopg2
pip3 install "fastapi[all]" SQLAlchemy psycopg2-binary

-- Atualizando a biblioteca do python (opcional)
python.exe -m pip install --upgrade pip

--Executa o comando python
python

--Importar o arquivo services
import services

-- Criar a tabela definida no arquivo services
services.\_add_tables()

--Nesse ponto, subimos a imagem do postgres, criamos um banco e uma tabela em branco.

-- Subindo a imagem do FastAPI

--Dentro do diretório com os arquivos, executar o comando:
uvicorn main:app --reload

Caso não funcione o comando a cima, rodar o código: python -m uvicorn main:app --reload

abrir no diretório o caminho http://127.0.0.1:8000 ou clicar no link
