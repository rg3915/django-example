#!python3
import io
import sys
import datetime
import names
from gen_random_values import *

type_phone_list = (
    ('pri'),
    ('com'),
    ('res'),
    ('cel'),
    ('cl'),
    ('oi'),
    ('t'),
    ('v'),
    ('n'),
    ('fax'),
    ('o'),
)

phone_list = []
repeat = 180
with io.open('fixtures/telefones.csv', 'wt') as f:
    f.write('id,person,phone,type_phone\n')
    for i in range(repeat):
        person = random.randint(1, 100)  # person registrados
        phone = gen_phone()
        type_phone = random.choice(type_phone_list)
        # id, person, phone, type_phone
        phone_list.append((i + 1, person, phone, type_phone))
    for l in phone_list:
        s = str(l[0]) + "," + str(l[1]) + "," + \
            str(l[2]) + "," + str(l[3]) + "\n"
        f.write(str(s))
