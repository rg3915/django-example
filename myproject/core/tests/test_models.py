from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from myproject.core.models import Person, Occupation, Address, Phone, Brand, Category, Product


class PersonModelTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(
            occupation='Web developer',
        )

        self.person = Person(
            occupation=self.occupation,
            gender='M',
            treatment='sr',
            first_name='Regis',
            last_name='da Silva',
            cpf='11122233396',
            birthday='1979-05-31T00:00:00+00:00',
            email='r.santos@example.com',
            blocked=False,
        )

    def test_create(self):
        """
        Person must have gender, first_name, last_name, cpf, birthday, email,
        phone, occupation, blocked
        """
        self.person.save()
        self.assertEqual(1, self.person.pk)

    def test_has_created_at(self):
        'Person must have automatic created_at.'
        self.person.save()
        self.assertIsInstance(self.person.created_at, datetime)

    # def test_str(self):
    #     pass


class PersonUniqueTest(TestCase):

    def setUp(self):
        # Create a first entry to force the collision.
        self.occupation = Occupation.objects.create(
            occupation='Web developer',
        )

        self.person = Person.objects.create(
            occupation=self.occupation,
            gender='M',
            treatment='sr',
            first_name='Regis',
            last_name='da Silva',
            cpf='11122233396',
            birthday='1979-05-31T00:00:00+00:00',
            email='r.santos@example.com',
            blocked=False,
        )

    def test_cpf_unique(self):
        'CPF must be unique'
        p = Person(
            occupation=self.occupation,
            gender='M',
            treatment='sr',
            first_name='Regis',
            last_name='da Silva',
            cpf='11122233396',
            birthday='1979-05-31T00:00:00+00:00',
            email='r.santos@example.com',
            blocked=False,
        )
        self.assertRaises(IntegrityError, p.save)


class OccupationModelTest(TestCase):

    def setUp(self):
        self.occupation = Occupation(
            occupation='Web developer',
        )

    def test_create(self):
        self.occupation.save()
        self.assertEqual(1, self.occupation.pk)


class AddressModelTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(
            occupation='Web developer',
        )

        self.person = Person.objects.create(
            occupation=self.occupation,
            gender='M',
            treatment='sr',
            first_name='Regis',
            last_name='da Silva',
            cpf='11122233396',
            birthday='1979-05-31T00:00:00+00:00',
            email='r.santos@example.com',
            blocked=False,
        )

    def test_address(self):
        """
        Address must have person_id, type_address, address, address_number,
        complement, district, city, uf, cep
        """
        address = Address.objects.create(
            person=self.person,
            type_address='c',
            address=u'Av. Paulista',
            address_number=721,
            complement=u'apto 313',
            district=u'Bela Vista',
            city=u'São Paulo',
            uf='SP',
            cep='01311-100',
        )
        self.assertEqual(1, address.pk)


class PhoneModelTest(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(
            occupation='Web developer',
        )

        self.person = Person.objects.create(
            occupation=self.occupation,
            gender='M',
            treatment='sr',
            first_name='Regis',
            last_name='da Silva',
            cpf='11122233396',
            birthday='1979-05-31T00:00:00+00:00',
            email='r.santos@example.com',
            blocked=False,
        )

    def test_phone(self):
        """ Phone must have person_id, phone, type_phone """
        phone = Phone.objects.create(
            person=self.person,
            phone='(11) 1234-5678',
            type_phone='pri',
        )
        self.assertEqual(1, phone.pk)


class BrandModelTest(TestCase):

    def setUp(self):
        self.brand = Brand(
            brand='ambrella',
        )

    def test_create(self):
        self.brand.save()
        self.assertEqual(1, self.brand.pk)


class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category(
            category='alimento',
        )

    def test_create(self):
        self.category.save()
        self.assertEqual(1, self.category.pk)


class ProductModelTest(TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(
            brand='ambrella',
        )
        self.category = Category.objects.create(
            category='alimento',
        )

    def test_create(self):
        """
        Product must have imported, outofline, ncm, category, brand,
        product, cost, icms, ipi, stock, stock_min
        """
        self.product = Product.objects.create(
            brand=self.brand,
            category=self.category,
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
        self.assertEqual(1, self.product.pk)


class ProductUniqueTest(TestCase):

    def setUp(self):
        # Create a first entry to force the collision.
        self.brand = Brand.objects.create(
            brand='ambrella',
        )
        self.category = Category.objects.create(
            category='alimento',
        )

        self.product = Product.objects.create(
            brand=self.brand,
            category=self.category,
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

    def test_product_unique(self):
        'product must be unique'
        p = Product(
            brand=self.brand,
            category=self.category,
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
        self.assertRaises(IntegrityError, p.save)
