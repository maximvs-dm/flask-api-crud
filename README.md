# Flask API - CRUD

API de exemplo para as aulas de desenvolvimento web da Faculdade Impacta

## Criando e ativando um ambiente virtual

### Alternativa A: com PIPENV (recomendado para projetos maiores)

PIPENV é um módulo que usa o próprio `pip` do Python para instalar as dependências, mas adicona uma camada de gerenciamento de versões, com ferramentas para resolução de conflito de versões entre sub-dependências.

1. Instalar o `pipenv`

```sh
pip install pipenv
ou
py -m pip install pipenv
```

2. Ativar ou criar o ambiente virtual (o pipenv automaticamente verifica se já existe um ambiente virtual para o diretório atual e ativa-o em caso afirmativo. Caso não exista, ele cria um antes de ativá-lo)

```sh
pipenv shell
ou
py -m pipenv shell
```

### Alternativa B: com VENV (visto em aula)

VENV é um pacote padrão (já vem com a instalação do Python nas versões mais recentes)

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

   1. (para a alternativa A: pipenv) Usando o gerenciador de pacotes: `pipenv` (para atualizações, depende de outra pessoa ter subido alterações no arquivo `Pipfile`)

   ```sh
   pipenv install --dev
   ```

   ou

   2. (para a alternativa B: venv) Usando o instalador de pacotes nativo do Python: `pip` (para atualizações, depende de outra pessoa ter subido alterações no arquivo `requirements.txt`)

   ```sh
   pip install -r requirements.txt
   ```

   obs: os arquivos requirements.txt e o arquivo `Pipfile.lock` não devem ser editados manualmente. O arquivo `requirements.txt` pode ser gerado com o comando `pip freeze > requirements.txt`, já o arquivo `Pipfile.lock` é gerado e atualizado ao executarmos diferentes comandos do pipenv, de maneira automática.

3. Executar o comando na Shell
   ```sh
   flask run
   ```

## Criar o banco de dados e realizar as migrações (executar apenas o passo 3 para rodar o projeto após baixar/atualizar o repositório do git)

1. Inicializar o banco de dados (esse passo só precisa ser executado caso esteja refazendo as migrações, após deletar a pasta `migrations` ou ao iniciar um projeto pela primeira vez em uma máquina - sem a pasta migrations ainda)

   ```sh
   flask db init
   ```

2. Criar as migrações (esse passo só precisa ser executado ao realizar alguma alteração nos modelos ou ao criar um projeto do zero - após o passo 1)

   ```sh
   flask db migrate
   ```

3. Executar as migrações para atualizar o banco de dados (executado para persistir no banco as alterações das migrações após o passo 2)

   ```sh
   flask db upgrade
   ```

4. Após alterações nas classes dos modelos que representam as tabelas no banco, isto é, adição/remoção de campos, inclusão exclusão de tabelas, alteração de nomes de tabelas ou campos, etc., é preciso re-executar os passos 2 e 3. (é possível executar o passo 2 diversas vezes para gerar diferentes migrações e depois realizar o passo 3 uma única vez no final, ou então executar o passo 3 após cada execução do passo 2, fica a critério do/a desenvolvedor/a)

## Acessando o Swagger do projeto:

[http://127.0.0.1:5000/swagger-ui/](http://127.0.0.1:5000/swagger-ui/)
