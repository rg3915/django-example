#!python3
import io
import sys
import rstr
import urllib.request
import json
from gen_random_values import *
from pprint import pprint


type_address_list = (
    ('i'),
    ('c'),
    ('r'),
    ('o'),
)


address_list = []
repeat = 20
print('\nwait...\n')
with io.open('fixtures/enderecos.csv', 'wt') as f:
    f.write(
        'id,type_address,address,address_number,district,city,uf,cep,person\n')
    for i in range(repeat):
        print(repeat - i)
        # le uma lista de ceps validos e escolhe um deles.
        p = io.open('fixtures/ceps.csv', 'rt', encoding='utf-8')
        linelist = p.readlines()
        l = random.randint(1, 848877)
        # retorna o cep no formato 00000000
        cep = linelist[l].split('\n')[0].strip("'")
        # acessa a url a seguir
        url = 'http://viacep.com.br/ws/' + str(cep) + '/json'
        resp = urllib.request.urlopen(url).read()
        # carrega o json
        data = json.loads(resp.decode('utf-8'))
        # pprint(data)

        type_address = random.choice(type_address_list)
        address = data['logradouro']
        address_number = random.randint(1, 9999)
        district = data['bairro']
        city = data['localidade']
        uf = data['uf']
        person = random.randint(1, 100)  # person registrados
        # id, type_address, address, address_number, district, city, uf, cep, person
        address_list.append(
            (i + 1, type_address, address, address_number, district, city, uf, cep, person))
    for l in address_list:
        s = str(l[0]) + "," + str(l[1]) + "," + \
            str(l[2]) + "," + str(l[3]) + "," + \
            str(l[4]) + "," + str(l[5]) + "," + \
            str(l[6]) + "," + str(l[7]) + "," + \
            str(l[8]) + "\n"
        f.write(str(s))
