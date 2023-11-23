# Flask API - CRUD

API de exemplo para as aulas de desenvolvimento web da Faculdade Impacta

## Criando e ativando um ambiente virtual

### Com PIPENV (recomendado para projetos maiores)

PIPENV é um módulo que usa o próprio `pip` do Python para instalar as dependências, mas adicona uma camada de gerenciamento de versões, com ferramentas para resolução de conflito de versões entre sub-dependências.

1. Instalar o `pipenv`

```sh
pip install pipenv
ou
py -m pip install pipenv
```

2. Ativar ou criar o ambiente virtual (o pipenv automaticamente verifica se já existe um ambiente virtual para o diretório atual e ativa-o em caso afirmativo. Caso não exista, ele já cria um antes de ativá-lo)

```sh
pipenv shell
ou
py -m pipenv shell
```

### Com VENV (visto em aula)

VENV é um pacote padrão (já vem com a intalação do Python nas versões mais recentes)

1. Criar o ambiente virtual

```sh
venv <venv_name>
ou
py -m  venv <venv_name>
```

2. Ativar o ambiente virtual

```sh
source ./<venv_name>/Scripts/Activate
```

## Como rodar o projeto (com o ambiente virtual ativo)

1. Ativar o ambiente virtual (ver seção anterior)

2. Instalar os requisitos (só precisa ser feito quando o ambiente é criado pela primeira vez ou quando há inclusão ou exclusão de uma dependência por outro colega que esteja trabalhando no mesmo projeto em outra máquina)

    1. Usando o instalador de pacotes nativo do Python: `pip` (para atualizações, depende de outra pessoa ter subido alterações no arquivo `requirements.txt`)
    ```sh
    pip install -r requirements.txt
    ```
    ou

    2. Usando o gerenciador de pacotes: `pipenv` (para atualizações, depende de outra pessoa ter subido alterações no arquivo `Pipfile`)
    ```sh
    pipenv install --dev
    ```

    obs: os arquivos requirements.txt e o arquivo `Pipfile.lock` não devem ser editados manualmente.

3. Executar o comando na Shell
    ```sh
    flask run
    ```

## Criar o banco de dados e realizar as migrações (executar apenas o passo 3 para rodar o projeto após baixar/atualizar o repositório do git)

1. Inicialisar o banco de dados (esse passo só precisa ser executado caso esteja refazendo as migrações, após deletar a pasta `migrations` ou ao criar um projeto novo do zero)
    ```sh
    flask db init
    ```

2. Criar as migrações (esse passo só precisa ser executado ao realizar alguma alteração nos modelos ou ao criar um projeto do zero - após o passo 1)
    ```sh
    flask db migrate
    ```

3. Executar as migrações para atualizar o banco de dados
    ```sh
    flask db upgrade
    ```

4. Após alterações nas classes dos modelos que representam as tabelas no banco, isto é, adição/remoção de campos, inclusão exclusão de tabelas, alteração de nomes de tabelas ou campos, etc., é preciso re-executar os passos 2 e 3.

## Acessando o Swagger do projeto: 

[http://127.0.0.1:5000/swagger-ui/](http://127.0.0.1:5000/swagger-ui/)
