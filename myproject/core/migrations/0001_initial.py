# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('type_address', models.CharField(max_length=1, choices=[('i', 'indefinido'), ('c', 'comercial'), ('r', 'residencial'), ('o', 'outros')], default='i', verbose_name='tipo de endereço')),
                ('address', models.CharField(max_length=80, verbose_name='endereço')),
                ('address_number', models.PositiveIntegerField(verbose_name='número')),
                ('complement', models.CharField(max_length=80, verbose_name='complemento')),
                ('district', models.CharField(max_length=80, verbose_name='bairro')),
                ('city', models.CharField(max_length=80, verbose_name='cidade')),
                ('uf', models.CharField(max_length=2, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], verbose_name='UF')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
            ],
            options={
                'verbose_name_plural': 'endereços',
                'verbose_name': 'endereço',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, verbose_name='marca')),
            ],
            options={
                'verbose_name_plural': 'marcas',
                'verbose_name': 'marca',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('category', models.CharField(max_length=30, verbose_name='categoria')),
            ],
            options={
                'verbose_name_plural': 'categorias',
                'verbose_name': 'categoria',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('occupation', models.CharField(max_length=30, verbose_name='Profissão')),
            ],
            options={
                'verbose_name_plural': 'profissões',
                'verbose_name': 'profissão',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='modificado em', auto_now=True)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'masculino'), ('F', 'feminino')], verbose_name='gênero')),
                ('treatment', models.CharField(max_length=4, choices=[('a', 'Arq.'), ('aa', 'Arqa.'), ('d', 'Dona'), ('dr', 'Dr.'), ('dra', 'Dra.'), ('e', 'Eng.'), ('p', 'Prof.'), ('pa', 'Profa.'), ('sr', 'Sr.'), ('sra', 'Sra.'), ('srta', 'Srta.')], verbose_name='tratamento')),
                ('firstname', models.CharField(max_length=30, verbose_name='nome')),
                ('lastname', models.CharField(max_length=30, verbose_name='sobrenome')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('birthdate', models.DateTimeField(verbose_name='nascimento')),
                ('email', models.EmailField(max_length=75, blank=True, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=18, blank=True, verbose_name='fone')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('blocked', models.BooleanField(default=False, verbose_name='bloqueado')),
                ('occupation', models.ForeignKey(to='core.Occupation', blank=True, verbose_name='profissão')),
            ],
            options={
                'verbose_name_plural': 'pessoas',
                'verbose_name': 'pessoa',
                'ordering': ['firstname'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='telefone')),
                ('type_phone', models.CharField(max_length=3, choices=[('pri', 'principal'), ('com', 'comercial'), ('res', 'residencial'), ('cel', 'celular'), ('cl', 'Claro'), ('oi', 'Oi'), ('t', 'Tim'), ('v', 'Vivo'), ('n', 'Nextel'), ('fax', 'fax'), ('o', 'outros')], default='pri', verbose_name='tipo de telefone')),
                ('person', models.ForeignKey(to='core.Person', related_name='pessoa_fone', verbose_name='pessoa')),
            ],
            options={
                'verbose_name_plural': 'telefones',
                'verbose_name': 'telefone',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='modificado em', auto_now=True)),
                ('imported', models.BooleanField(default=False, verbose_name='importado')),
                ('outofline', models.BooleanField(default=False, verbose_name='fora de linha')),
                ('ncm', models.CharField(max_length=8, verbose_name='NCM')),
                ('product', models.CharField(max_length=80, unique=True, verbose_name='produto')),
                ('cost', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='custo')),
                ('icms', models.DecimalField(max_digits=3, decimal_places=2, verbose_name='ICMS')),
                ('ipi', models.DecimalField(max_digits=3, decimal_places=2, verbose_name='IPI')),
                ('stock', models.PositiveIntegerField(verbose_name='estoque atual')),
                ('stock_min', models.PositiveIntegerField(default=0, verbose_name='estoque mínimo')),
                ('brand', models.ForeignKey(to='core.Brand', related_name='marca', verbose_name='marca')),
                ('category', models.ForeignKey(to='core.Category', related_name='categoria', verbose_name='categoria')),
            ],
            options={
                'verbose_name_plural': 'produtos',
                'verbose_name': 'produto',
                'ordering': ['product'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(to='core.Person', related_name='pessoa_endereco', verbose_name='pessoa'),
            preserve_default=True,
        ),
    ]
