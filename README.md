# Simple Flask API

API de exemplo para as aulas de desenvolvimento web da Faculdade Impacta

## Como rodar o projeto

1. **Se estiver em um ambiente virtual, ativar o ambiente**

    1. Com `venv`
    ```sh
    source ./<venv_name>/Scripts/Activate
    ```

    ou 
    2. Com `pipenv`
    ```sh
    pipenv shell
    ou
    py -m pipenv shell
    ```


2. Instalar os requisitos

    1. Usando o instalador de pacotes nativo do Python: `pip`
    ```sh
    pip install -r requirements.txt
    ```
    ou

    2. Usando o gerenciador de pacotes: `pipenv`
    ```sh
    pipenv install --dev
    ```

3. copiar e executar os comandos a seguir no terminal/shell
    ```sh
    export FLASK_APP=app
    export FLASK_ENV=Development
    export FLASK_DEBUG=True
    ```

4. Executar o comando na Shell
    ```sh
    flask run
    ```

## Criar o banco de dados e realizar as migrações

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

4. Após alterações nas classes dos modelos que representam as tabelas no banco, isto é, adição/remoção de campos, inclusão exclusão de tabelas, alteração de nomes de tabelas ou campos, etc., é preciso re-executar os passos 2 e 3.
