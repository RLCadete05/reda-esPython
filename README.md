# Projeto redações

## Instalação das dos projeto dependências

Rode o comando `pip3 install pipenv` caso não tenha o pipenv. Instale as dependências do projeto com `pipenv install`.

## Subindo o banco de dados

Rode `docker-compose up -d` para subir o banco Postgres na porta `5432` e o gerenciador para verificar os dados na porta `8080` que pode ser acessado em `http://localhost:8080`, para poder ter acesso ao banco de dados, marque `postgresSql` em host coloque `pgsql`, em user `pguser`, em password coloque `pgpassword` e em database coloque `redacoes` (caso dê erro no banco, faça login sem informar o mesmo), para verificar. (Caso use linux, utilize o `sudo` antes).

## Rodar o projeto

`pipenv shell` para entrar na maquiva virtual com suas dependências instaladas, após isso basta rodar `python3 index.py` para rodar o arquivo que você precisa.

## Instalação de nova dependência no projeto

`pipenv install nome-pacote`
