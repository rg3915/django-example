#!python3
import io
import sys
import datetime
import names
from gen_random_values import *

""" List of values for use in choices in models. """
treatment_male_list = (
    ('a'),
    ('dr'),
    ('e'),
    ('p'),
    ('sr'),
)

treatment_female_list = (
    ('aa'),
    ('d'),
    ('ea'),
    ('pa'),
    ('sra'),
    ('srta'),
)

person_list = []
repeat = 100
with io.open('fixtures/pessoas.csv', 'wt') as f:
    f.write(
        'id,gender,treatment,firstname,lastname,cpf,birthdate,email,occupation,active,blocked,created_at,modified_at\n')
    for i in range(repeat):
        g = random.choice(['M', 'F'])
        if g == 'M':
            treatment = random.choice(treatment_male_list)
            firstname = names.get_first_name(gender='male')
        else:
            treatment = random.choice(treatment_female_list)
            firstname = names.get_first_name(gender='female')
        lastname = names.get_last_name()
        cpf = gen_cpf()
        birthdate = gen_timestamp() + '+00'
        email = firstname[0].lower() + '.' + lastname.lower() + '@example.com'
        occupation = random.randint(1, 163)  # occupation registrados
        active = random.choice(['True', 'False'])
        blocked = random.choice(['True', 'False'])
        date = datetime.datetime.now().isoformat(" ") + "+00"
        # id,gender,treatment,firstname,lastname,cpf,birthdate,email,occupation,active,blocked,created_at,modified_at
        person_list.append(
            (i + 1, g, treatment, firstname, lastname, cpf, birthdate, email, occupation, active, blocked, date, date))
    for l in person_list:
        s = str(l[0]) + "," + str(l[1]) + "," + str(l[2]) + "," + str(l[3]) \
            + "," + str(l[4]) + "," + str(l[5]) + "," + str(l[6]) + "," + str(l[7]) \
            + "," + str(l[8]) + "," + str(l[9]) + "," + \
            str(l[10]) + "," + str(l[11]) + "," + \
            str(l[12]) + "\n"
        f.write(str(s))
