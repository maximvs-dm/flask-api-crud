# Simple Flask API

API de exemplo para as aulas de desenvolvimento web da Faculdade Impacta

## Como rodar o projeto

1. Instalar os requisitos

2. **Se estiver em um ambiente virtual, ativar o ambiente**

3. copiar e executar os comandos a seguir na Shell

    ```sh
    export FLASK_APP=app
    export FLASK_ENV=Development
    export FLASK_DEBUG=True
    ```

4. Executar o comando na Shell

    ```sh
    flask run
    ```

## Criar o banco de dados e realizar migrações

1. Inicialisar o banco de dados

    ```sh
    flask db init
    ```

2. Criar a primeira migração

    ```sh
    flask db migrate
    ```

3. Executar a primeira migração para atualizar o banco de dados

    ```sh
    flask db upgrade
    ```
