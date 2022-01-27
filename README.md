# agenda_django
Agenda Python Django

A propósito do curso Udemy que segui com o mestre Luíz Otávio Miranda, um dos projetos padrão Django que construimos de raiz, é este.   
Uma agenda de contactos construída em Django para ser alojada num qualquer domínio. Está pronto a ser melhorado à medida que for aprendendo mais Django e descobrindo melhoramentos a fazer.

## Dependências   
As dependências do projeto estão descritas no ficheiro requirements.txt. Se pretender utilizar um ambiente virtual, deverá correr na raíz do projeto os comandos:   
- python3 -m venv venv/
- source venv/bin/activate   
E depois então correr o comando pip para instalar as dependências listadas no ficheiro **requirements.txt** apenas no ambiente virtual e não globalmente no seu sistema operativo.


## Instruções de instalação   
Para correr o projeto, depois de fazer git clone, é necessário usar o ***pip*** para instalar as dependências. Depois disso, o projeto está configurado para utilizar uma base de dados ***SQLite3***.com um ficheiro criado na raíz do projeto de nome **"db.sqlite3"**.   
Para uma utilização como superuser de forma a aceder à área administrativa em **localhost:8000/admin/** é necessário criar um com o comando:
- python3 manage.py createsuperuser

Para criar a estrutura da base de dados necessária é necessário correr as migrações com os comandos:
- python3 manage.py makemigrations
- python3 manage.py migrate

Após criado o utilizador e feitas as migrações, é possível correr o servidor com o comando: ***python3 manage.py runserver***


**Author:**   
João Ramos
