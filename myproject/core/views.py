from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Person, Occupation, Address, Phone, Product, Brand, Category


def home(request):
    return render(request, 'home.html')


class PersonList(ListView):
    template_name = 'core/person/person_list.html'
    model = Person
    paginate_by = 10

    def get_queryset(self):
        persons = Person.objects.all()
        var_get_search = self.request.GET.get('search_box')
        if var_get_search is not None:
            persons = persons.filter(firstname__icontains=var_get_search)
        return persons


class PersonForm(CreateView):
    template_name = 'core/person/person_form.html'
    model = Person
    success_url = reverse_lazy('person_list')


class OccupationForm(CreateView):
    template_name = 'core/person/occupation_form.html'
    model = Occupation
    success_url = reverse_lazy('occupation_list')


class AddressForm(CreateView):
    template_name = 'core/person/address_form.html'
    model = Address
    success_url = reverse_lazy('home')


class PhoneForm(CreateView):
    template_name = 'core/person/phone_form.html'
    model = Phone
    success_url = reverse_lazy('home')


class ProductList(ListView):
    template_name = 'core/product/product_list.html'
    model = Product
    paginate_by = 10

    def get_queryset(self):
        products = Product.objects.all()
        var_get_search = self.request.GET.get('search_box')
        if var_get_search is not None:
            products = products.filter(product__icontains=var_get_search)
        return products


class ProductForm(CreateView):
    template_name = 'core/product/product_form.html'
    model = Product
    success_url = reverse_lazy('product_list')


class BrandForm(CreateView):
    template_name = 'core/product/brand_form.html'
    model = Brand
    success_url = reverse_lazy('brand_list')


class CategoryForm(CreateView):
    template_name = 'core/product/category_form.html'
    model = Category
    success_url = reverse_lazy('category_list')


def download(request):
    return render(request, 'download.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
