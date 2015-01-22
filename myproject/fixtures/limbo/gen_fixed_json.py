#!python3
import io
import sys
import datetime
import names
from gen_random_values import *

occupation_list = []
occupation_repeat = 163


def read_occupation():
    with io.open('fixtures/profissoes.json', 'wt') as f:
        for i in range(occupation_repeat):
            r = io.open('fixtures/profissoes.csv', 'rt', encoding='utf-8')
            linelist = r.readlines()
            occupation = linelist[i].split('\n')[0].strip("'")
            print(occupation)

            # for i in range(occupation_repeat):
            occupation_list.append((i + 1, occupation))
        f.write('[\n')
        for l in occupation_list:
            s = "{\n" + \
                str('  "pk": ') + str(l[0]) + ",\n" + \
                str('  "model": "core.occupation",\n') + \
                str('  "fields": {\n') + \
                str('    "occupation": "') + l[1] + str('"\n') + \
                "  }\n"
            if l[0] == occupation_repeat:
                s = s + "}\n"
            else:
                s = s + "},\n"
            f.write(str(s))
        f.write(']\n')

if __name__ == '__main__':
    read_occupation()
