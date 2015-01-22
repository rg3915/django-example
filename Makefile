install:
	pip install -r requirements.txt
	# pip install -Iv https://pypi.python.org/packages/source/p/pyparsing/pyparsing-2.0.3.tar.gz#md5=0fe479be09fc2cf005f753d3acc35939
	# pip install -Iv https://pypi.python.org/packages/source/p/pygraphviz/pygraphviz-1.3rc2.tar.gz#md5=061ff5c4b8ea4b7cd05be0588172ef07
	# pip install -Iv http://code.google.com/p/pydot/downloads/detail?name=pydot-1.0.25.tar.gz&can=2&q=
	# pip install pydot
	# pip freeze > requirements.txt

create:
	python manage.py makemigrations core
	python manage.py migrate
	python manage.py createsuperuser

mer:
	python manage.py graph_models -e -g -l dot -o modelagem/core.png core

setup: install create
