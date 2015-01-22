# -*- coding: utf-8 -*-
from model_mommy import mommy
from myproject.core.models import Person, Occupation, Address, Phone, Product, Brand, Category
import names

customers = mommy.make(
    Person, firstname=names.get_first_name, lastname=names.get_last_name, _quantity=20)
occupation = mommy.make(Occupation, _quantity=10)
address = mommy.make(Address, _quantity=10)
phone = mommy.make(Phone, _quantity=10)
product = mommy.make(Product, _quantity=10)
brand = mommy.make(Brand, _quantity=10)
category = mommy.make(Category, _quantity=10)
