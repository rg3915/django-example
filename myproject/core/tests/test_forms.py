from django.test import TestCase
from myproject.core.forms import PersonForm, AddressForm, ProductForm


class PersonFormTest(TestCase):

    # def test_cpf_is_digit(self):
    #     'CPF must only accept digits.'
    #     form = self.make_validated_form(cpf='ABCD0000000')
    #     self.assertItemsEqual(['cpf'], form.errors)

    # def test_cpf_has_11_digits(self):
    #     'CPF must have 11 digits.'
    #     form = self.make_validated_form(cpf='1234')
    #     self.assertItemsEqual(['cpf'], form.errors)

    def test_name_must_be_capitalized(self):
        'Name must be capitalized.'
        form = self.make_validated_form(name='REGIS')
        self.assertEqual('Regis', form.cleaned_data['first_name'])

    def make_validated_form(self, **kwargs):
        data = dict(
            occupation=1,
            gender='M',
            treatment='sr',
            first_name='Regis',
            last_name='da Silva',
            cpf='11122233396',
            birthday='1979-05-31T00:00:00+00:00',
            email='r.santos@example.com',
            phone=1,
            blocked=False,
        )
        data.update(kwargs)
        form = PersonForm(data)
        form.is_valid()
        return form


class AddressFormTest(TestCase):

    def make_validated_form(self, **kwargs):
        data = dict(
            person=1,
            type_address='c',
            address=u'Av. Paulista',
            address_number=721,
            complement=u'apto 313',
            district=u'Bela Vista',
            city=u'São Paulo',
            uf='SP',
            cep='01311-100',
        )
        data.update(kwargs)
        form = AddressForm(data)
        form.is_valid()
        return form


class ProductFormTest(TestCase):

    def make_validated_form(self, **kwargs):
        data = dict(
            brand=1,
            category=1,
            imported=True,
            outofline=False,
            ncm='12345678',
            product=u'Amendoim',
            cost=5.75,
            icms=0.05,
            ipi=0.1,
            stock=100,
            stock_min=50,
        )
        data.update(kwargs)
        form = ProductForm(data)
        form.is_valid()
        return form
