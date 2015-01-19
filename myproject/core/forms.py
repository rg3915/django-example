from django.forms import ModelForm
from .models import Person, Occupation, Address, Phone, Product, Brand, Category


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = '__all__'


class OccupationForm(ModelForm):

    class Meta:
        model = Occupation
        fields = '__all__'


class AddressForm(ModelForm):

    class Meta:
        model = Address
        fields = '__all__'


class PhoneForm(ModelForm):

    class Meta:
        model = Phone
        fields = '__all__'


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class BrandForm(ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'


class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
