 ## Login e Postagem de alunos
 
Aprendendo a utilizar o framework web Django. Foi-se utilizado de técnicas, como:
  * Classes (OO)
  * Configuração de Rotas
  * Separação de [APP's](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
  * Padrão MVC
  * Organização de arquivos estáticos
  * [Jinja Format](https://jinja.palletsprojects.com/en/2.11.x/templates/)
  * Criação de usuário ADM para o Django
  * Criação de usuário com [biblioteca do Django](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/)
  * *Decorators*
  * Login e Log Out
  * Integração com BD relacional
  * CRUD
  * Migrations
  * Mensagens personalizadas (Erro, aviso, etc...)
  * Tratamento de requisições
 
 
## Tecnologias 
 
Tecnologias utilizadas no projeto.
 
* Python version  3.8.5
* Django version 3.1.4
 * [Jinja Format](https://jinja.palletsprojects.com/en/2.11.x/templates/)
* Bootstrap 4
* Postgres Alpine (Imagem Docker) 13.2
* Docker 20.10.4
 
 
## Services Used
 
* Github
 
## Pip
 Você vai precisar de algumas libs para rodar o projeto. Os requerimentos estarão no arquivo [requeriments.txt](https://github.com/Jackie098/django-example/blob/master/requeriments.txt).

 Para instalar os requerimentos, basta rodar no terminal:
 > $ pip install -r requeriments.txt
  
  ATENÇÃO: Considere estar na mesma pasta do 'requeriments.txt'.

  Se você usa ambiente virtual (o recomendado):
  1. Instale o ambiente virtual:
  > $ python3 -m venv myvenv
  2. Inicie o ambiente. Se atente em colocar o caminho correto do arquivo:
  > $ source ./myvenv/bin/activate
  3. Depois de clonar o repositório, instale as dependências com o arquivo 'requeriments.txt':
  > $ pip install -r requeriments.txt
 
## Começando
 
* Considere os passos anteriores na sessão **PIP**.
* O seu banco de dados deve estar sincronizado. Para isso, crie um banco de dados **Postgree** chamado *homebroke*, atente-se para estar na porta *5432* e configure o restante das informações de acordo com o seu ambiente.
* Assim que o banco de dados estiver conectado, insira o comando no terminal:
> $ python manage.py migrate

Você deve estar no mesmo nível do diretório do arquivo *manage.py*. Se houver algum problema, tente executar estes dois comandos a seguir no terminal:
**1º**
> $ python manage.py makemigrations

**2º**
> $ python manage.py migrate
* Agora com o banco conectado e todas as tabelas criadas, inicie o servidor:
> $ python manage.py runserver

Se estiver utilizando, certifique-se de estar com o ambiente virtual rodando e na mesma pasta do arquivo **manage.py**.

## Como usar
 
 Com o servidor rodando, crie uma conta através do link no *nav-bar* ao lado do botão verde de *login*.
 ![Cadastro de usuário](https://github.com/Jackie098/django-example/blob/master/images-readme/cadastro-usuario.png)

 Com uma conta já criada, faça *login*.
 ![Usuário logado](https://github.com/Jackie098/django-example/blob/master/images-readme/usuario-logado.png)

 Após o *login*, observe que os botões ao canto superior direito mudaram e no canto superior esquerdo apareceu a opção de criar postagem.
 ![Cadastro de usuário](https://github.com/Jackie098/django-example/blob/master/images-readme/criando-postagem.png)

 *Foi adicionado mais um link para visualização das postagens*
 
## Atualizações
 
  - Sugestões: 
    - Adicionar funcionalidades na sessão HOME
    - Pode-se exibir os posts de cada aluno (como um feed ou um fórum)
    - Melhorar a classe POST: Atribuir outros tipos de campos
    - Criar um APP e/ou classe para a interação de vários alunos no feed (como numa rede social)
 
 
## Links
 
  - Repositório: https://github.com/Jackie098/django-example
    - Em caso de dúvidas ou sugestões, sinta-se livre para entrar em contato e/ou solicitar **pull requests**.
 
 
## Autor
 
* **Carlos Augusto M**: @Jackie098 (https://github.com/Jackie098)