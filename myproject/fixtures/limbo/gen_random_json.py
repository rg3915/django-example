#!python3
import io
import sys
import datetime
import names
from gen_random_values import *

lista = []
repeat = 100
with io.open('fixtures.json', 'wt') as f:
    for i in range(repeat):
        date = datetime.datetime.now().isoformat(" ")
        fname = names.get_first_name()
        lname = names.get_last_name()
        email = fname[0].lower() + '.' + lname.lower() + '@email.com'
        b = random.choice(['true', 'false'])
        # pk, firstname, lastname, cpf, birthdate, email, phone, blocked,
        # created_at, modified_at
        lista.append(
            (i + 1, fname, lname, gen_cpf(), gen_timestamp(), email, gen_phone(), b, date, date))
    f.write('[\n')
    for l in lista:
        s = "{\n" + \
            str('  "pk": ') + str(l[0]) + ",\n" + \
            str('  "model": "core.person",\n') + \
            str('  "fields": {\n') + \
            str('    "firstname": "') + l[1] + str('",\n') + \
            str('    "lastname": "') + l[2] + str('",\n') + \
            str('    "cpf": "') + l[3] + str('",\n') + \
            str('    "birthdate": "') + l[4] + str('",\n') + \
            str('    "email": "') + l[5] + str('",\n') + \
            str('    "phone": "') + l[6] + str('",\n') + \
            str('    "blocked": ') + l[7] + str(',\n') + \
            str('    "created_at": "') + l[8] + str('",\n') + \
            str('    "modified_at": "') + l[9] + str('"\n') + \
            "  }\n"
        if l[0] == repeat:
            s = s + "}\n"
        else:
            s = s + "},\n"
        f.write(str(s))
    f.write(']\n')
