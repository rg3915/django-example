occupation:
	python csv2json.py fixtures/profissoes.csv core.Occupation

load_occupation:
	python ../../manage.py loaddata fixtures/profissoes.csv.json

brand:
	python csv2json.py fixtures/marcas.csv core.Brand

load_brand:
	python ../../manage.py loaddata fixtures/marcas.csv.json

category:
	python csv2json.py fixtures/categorias.csv core.Category

load_category:
	python ../../manage.py loaddata fixtures/categorias.csv.json

product:
	python gen_products_csv.py
	python csv2json.py fixtures/produtos.csv core.Product

load_product:
	python ../../manage.py loaddata fixtures/produtos.csv.json

person:
	python gen_persons_csv.py
	python csv2json.py fixtures/pessoas.csv core.Person

load_person:
	python ../../manage.py loaddata fixtures/pessoas.csv.json

address:
	python gen_address_csv.py
	python csv2json.py fixtures/enderecos.csv core.Address

load_address:
	python ../../manage.py loaddata fixtures/enderecos.csv.json

phone:
	python gen_phones_csv.py
	python csv2json.py fixtures/telefones.csv core.Phone

load_phone:
	python ../../manage.py loaddata fixtures/telefones.csv.json

gen_fixtures: occupation person address phone load_occupation load_person load_address load_phone

load_fixtures: brand category product load_brand load_category load_product