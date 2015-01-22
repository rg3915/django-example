#!python3
import io
import sys
import datetime
import names
from gen_random_values import *

product_list = []
repeat = 100
with io.open('fixtures/produtos.csv', 'wt') as f:
    f.write(
        'id,imported,outofline,ncm,category,brand,product,cost,icms,ipi,stock,stock_min,created_at,modified_at\n')
    for i in range(repeat):
        imported = random.choice(['True', 'False'])
        outofline = random.choice(['True', 'False'])
        ncm = gen_ncm()
        category = random.randint(1, 23)
        brand = random.randint(1, 20)
        # le uma lista de produtos.
        p = io.open('fixtures/produtos1.csv', 'rt', encoding='utf-8')
        linelist = p.readlines()

        product = linelist[i].split('\n')[0]
        cost = gen_decimal(4, 2)

        ipi = 0
        # para o ipi ficar abaixo de 0.5
        if imported == 'True':
            ipi = float(gen_ipi())
            if ipi > 0.5:
                ipi = ipi - 0.5

        icms = gen_ipi()
        stock = random.randint(1, 200)
        stock_min = random.randint(1, 20)
        date = datetime.datetime.now().isoformat(" ") + "+00"
        # id, imported, outofline, ncm, category_id, brand_id, product, cost, icms, ipi, stock, stock_min, created_at, modified_at
        product_list.append(
            (i + 1, imported, outofline, ncm, category, brand, product, cost, icms, ipi, stock, stock_min, date, date))
    for l in product_list:
        s = str(l[0]) + "," + str(l[1]) + "," + str(l[2]) + "," + str(l[3]) \
            + "," + str(l[4]) + "," + str(l[5]) + "," + str(l[6]) + "," + str(l[7]) \
            + "," + str(l[8]) + "," + str(l[9]) + "," + \
            str(l[10]) + "," + str(l[11]) + "," + \
            str(l[12]) + "," + str(l[13]) + "\n"
        f.write(str(s))
