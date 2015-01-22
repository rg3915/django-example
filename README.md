# django-example

A complete example for modelling in Django 1.7

## Baixando e rodando a app

	$ git clone https://github.com/rg3915/django-example.git
	$ virtualenv -p /usr/bin/python3 django-example
	$ cd django-example
	$ source bin/activate

Para diminuir o caminho do prompt digite (opcional)
	
	$ PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ "

Instalando as dependências e continuando

	$ make setup
	$ python manage.py test
	$ cd myproject/fixtures
	$ make gen_fixtures # gerando fixtures
	$ make load_fixtures
	$ cd ..
	$ cd ..
	$ python manage.py runserver