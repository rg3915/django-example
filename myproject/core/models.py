# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.formats import number_format
# List of values for use in choices
from .applib.lists import gender_list, treatment_list, type_address_list, uf_list, type_phone_list


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        _('criado em'), auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(
        _('modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Person(TimeStampedModel):
    gender = models.CharField(_(u'gênero'), max_length=1, choices=gender_list)
    treatment = models.CharField(
        _('tratamento'), max_length=4, choices=treatment_list)
    first_name = models.CharField(_('nome'), max_length=30)
    last_name = models.CharField(_('sobrenome'), max_length=30)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    birthday = models.DateTimeField(_('nascimento'))
    email = models.EmailField(_('e-mail'))
    occupation = models.ForeignKey(
        "Occupation", verbose_name=_(u'profissão'))
    active = models.BooleanField(_('ativo'), default=True)
    blocked = models.BooleanField(_('bloqueado'), default=False)

    class Meta:
        ordering = ['first_name']
        verbose_name = "pessoa"
        verbose_name_plural = "pessoas"

    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    full_name = property(__str__)


class Occupation(models.Model):
    occupation = models.CharField(_(u'Profissão'), max_length=30)

    class Meta:
        ordering = ['occupation']
        verbose_name = u"profissão"
        verbose_name_plural = u"profissões"

    def __str__(self):
        return self.occupation


class Address(models.Model):
    type_address = models.CharField(
        _(u'tipo de endereço'), max_length=1, choices=type_address_list, default='i')
    address = models.CharField(_(u'endereço'), max_length=80)
    address_number = models.PositiveIntegerField(_(u'número'))
    complement = models.CharField(_('complemento'), max_length=80, blank=True)
    district = models.CharField(_('bairro'), max_length=80)
    city = models.CharField(_('cidade'), max_length=80)
    uf = models.CharField(_('UF'), max_length=2, choices=uf_list)
    cep = models.CharField(_('CEP'), max_length=9)
    person = models.ForeignKey(
        "Person", verbose_name='pessoa', related_name=_('pessoa_endereco'))

    class Meta:
        verbose_name = u"endereço"
        verbose_name_plural = u"endereços"

    def __str__(self):
        return self.cep


class Phone(models.Model):
    person = models.ForeignKey(
        "Person", verbose_name='pessoa', related_name=_('pessoa_fone'))
    phone = models.CharField(_('telefone'), max_length=20)
    type_phone = models.CharField(
        _('tipo de telefone'), max_length=3, choices=type_phone_list, default='pri')

    class Meta:
        verbose_name = "telefone"
        verbose_name_plural = "telefones"

    def __str__(self):
        return self.phone


class Brand(models.Model):
    brand = models.CharField(_('marca'), max_length=30)

    class Meta:
        ordering = ['brand']
        verbose_name = "marca"
        verbose_name_plural = "marcas"

    def __str__(self):
        return self.brand


class Category(models.Model):
    category = models.CharField(_('categoria'), max_length=30)

    class Meta:
        ordering = ['category']
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.category


class Product(TimeStampedModel):
    imported = models.BooleanField(_('importado'), default=False)
    outofline = models.BooleanField(_('fora de linha'), default=False)
    ncm = models.CharField(_('NCM'), max_length=8)
    category = models.ForeignKey(
        "Category", verbose_name='categoria', related_name='categoria')
    brand = models.ForeignKey(
        "Brand", verbose_name='marca', related_name='marca')
    product = models.CharField(_('produto'), max_length=80, unique=True)
    cost = models.DecimalField(_('custo'), max_digits=8, decimal_places=2)
    icms = models.DecimalField(_('ICMS'), max_digits=3, decimal_places=2)
    ipi = models.DecimalField(_('IPI'), max_digits=3, decimal_places=2)
    stock = models.PositiveIntegerField(_('estoque atual'))
    stock_min = models.PositiveIntegerField(_(u'estoque mínimo'), default=0)

    class Meta:
        ordering = ['product']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.product

    def get_cost(self):
        return u"R$ %s" % number_format(self.cost, 2)

    def get_icms(self):
        return u"%s" % number_format(self.icms * 100, 0)

    def get_ipi(self):
        return u"%s" % number_format(self.ipi * 100, 0)
