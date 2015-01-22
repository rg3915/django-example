from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Person, Occupation, Address, Phone, Product, Brand, Category


def home(request):
    return render(request, 'index.html')


class PersonList(ListView):
    template_name = 'core/person/person_list.html'
    model = Person
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['name'] = 'pessoa'
        context['name_plural'] = 'pessoas'
        return context

    def get_queryset(self):
        persons = Person.objects.all()
        var_get_search = self.request.GET.get('search_box')
        if var_get_search is not None:
            persons = persons.filter(firstname__icontains=var_get_search)
        return persons


class PersonCreate(CreateView):
    template_name = 'core/person/person_create_form.html'
    model = Person
    success_url = reverse_lazy('person_list')

    def get_context_data(self, **kwargs):
        context = super(PersonCreate, self).get_context_data(**kwargs)
        context['name'] = 'pessoa'
        return context


class OccupationList(ListView):
    template_name = 'core/person/occupation_list.html'
    model = Occupation
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(OccupationList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['name'] = u'profissão'
        context['name_plural'] = u'profissões'
        return context

    def get_queryset(self):
        occupations = Occupation.objects.all()
        var_get_search = self.request.GET.get('search_box')
        if var_get_search is not None:
            occupations = occupations.filter(
                occupation__icontains=var_get_search)
        return occupations


class OccupationCreate(CreateView):
    template_name = 'core/person/occupation_create_form.html'
    model = Occupation
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(OccupationCreate, self).get_context_data(**kwargs)
        context['name'] = u'profissão'
        return context


class AddressCreate(CreateView):
    template_name = 'core/person/address_create_form.html'
    model = Address
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(AddressCreate, self).get_context_data(**kwargs)
        context['name'] = u'endereço'
        return context


class PhoneCreate(CreateView):
    template_name = 'core/person/phone_create_form.html'
    model = Phone
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(PhoneCreate, self).get_context_data(**kwargs)
        context['name'] = 'telefone'
        return context


class ProductList(ListView):
    template_name = 'core/product/product_list.html'
    model = Product
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['name'] = 'produto'
        context['name_plural'] = 'produtos'
        return context

    def get_queryset(self):
        products = Product.objects.all()
        var_get_search = self.request.GET.get('search_box')
        if var_get_search is not None:
            products = products.filter(product__icontains=var_get_search)
        return products


class ProductCreate(CreateView):
    template_name = 'core/product/product_create_form.html'
    model = Product
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super(ProductCreate, self).get_context_data(**kwargs)
        context['name'] = 'produto'
        return context


class BrandList(ListView):
    template_name = 'core/product/brand_list.html'
    model = Brand
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(BrandList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['name'] = 'marca'
        context['name_plural'] = 'marcas'
        return context

    def get_queryset(self):
        brands = Brand.objects.all()
        var_get_search = self.request.GET.get('search_box')
        if var_get_search is not None:
            brands = brands.filter(brand__icontains=var_get_search)
        return brands


class BrandCreate(CreateView):
    template_name = 'core/product/brand_create_form.html'
    model = Brand
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(BrandCreate, self).get_context_data(**kwargs)
        context['name'] = 'marca'
        return context


class CategoryList(ListView):
    template_name = 'core/product/category_list.html'
    model = Category
    paginate_by = 23

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['name'] = 'categoria'
        context['name_plural'] = 'categorias'
        return context

    def get_queryset(self):
        categorys = Category.objects.all()
        var_get_search = self.request.GET.get('search_box')
        if var_get_search is not None:
            categorys = categorys.filter(category__icontains=var_get_search)
        return categorys


class CategoryCreate(CreateView):
    template_name = 'core/product/category_create_form.html'
    model = Category
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(CategoryCreate, self).get_context_data(**kwargs)
        context['name'] = 'categoria'
        return context


def download(request):
    return render(request, 'download.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
