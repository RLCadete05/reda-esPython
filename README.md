# Projeto redações

## Instalação das dos projeto dependências

1 - Rode o comando `pip3 install pipenv` caso não tenha o pipenv.
2 - Instale as dependências do projeto com `pipenv install`.
3 - Rode `docker-compose up -d` para subir o banco Postgres na porta `5432` e o gerenciador para verificar os dados na porta `8080` que pode ser acessado em `http://localhost:8080`. (Caso use linux, utilize o sudo antes)

## Instalação de nova dependência no projeto

1 - `pipenv install nome-pacote`

## Rodar o projeto

1 - `pipenv shell`
