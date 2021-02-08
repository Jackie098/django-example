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
 
 
## Services Used
 
* Github
 
## Pip
 Você vai precisar de algumas libs para rodar o projeto. Os requerimentos estarão no arquivo [requeriments.txt](https://github.com/Jackie098/django-example/blob/master/requeriments.txt).

 Para instalar os requerimentos, basta rodar no terminal:
 > $ pip install requeriments.txt
  
  ATENÇÃO: Considere estar na mesma pasta do 'requeriments.txt'.

  Se você usa ambiente virtual (o recomendado):
  1. Instale o ambiente virtual:
  > $ python3 -m venv myvenv
  2. Inicie o ambiente. Se atente em colocar o caminho correto do arquivo:
  > $ source ./myvenv/bin/activate
  3. Depois de clonar o repositório, instale as dependências com o arquivo 'requeriments.txt':
  > $ pip install requeriments.txt
 
## Começando
 
* Considere os passos anteriores na sessão **PIP**. Em seguida:
>    $ python manage.py runserver

  Se estiver utilizando, certifique-se de estar com o ambiente virtual rodando e na mesma pasta do arquivo **manage.py**.

## Como usar
 
 Com o servidor rodando, crie uma conta através do link no *nav-bar* ao lado do botão verde de *login*.
 ![Cadastro de usuário](./images-readme/cadastro-usuario)

 Com uma conta já criada, faça *login*.
 ![Usuário logado](./images-readme/cadastro-usuario)

 Após o *login*, observe que os botões ao canto superior direito mudaram e no canto superior esquerdo apareceu a opção de criar postagem.
 ![Cadastro de usuário](./images-readme/cadastro-usuario)
 
 
## Atualizações
 
  - Sugestões: 
    - Pode-se exibir os posts de cada aluno (como um feed) na seção HOME
    - Melhorar a classe POST: Atribuir outros tipos de campos
    - Criar um APP e/ou classe para a interação de vários alunos no feed (como numa rede social)
 
 
## Links
 
  - Repositório: https://github.com/Jackie098/django-example
    - Em caso de dúvidas ou sugestões, sinta-se livre para entrar em contato e/ou solicitar **pull requests**.
 
 
## Autor
 
* **Carlos Augusto M**: @Jackie098 (https://github.com/Jackie098)