from django.contrib import admin
from .models import Person, Occupation, Address, Phone, Brand, Category, Product


class PersonAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Person model"""
    ordering = ['firstname']
    list_display = (
        '__str__', 'cpf', 'email', 'occupation', 'created_at', 'active', 'blocked')
    date_hierarchy = 'created_at'
    search_fields = ('firstname', 'lastname')
    list_filter = ('gender', 'active', 'blocked',)


class AddressAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Address model"""
    ordering = ['person']
    list_display = (
        'person', 'address', 'district', 'city', 'uf', 'cep', 'type_address')
    search_fields = (
        'person__firstname', 'address', 'district', 'city', 'cep')
    list_filter = ('type_address', 'uf')


class PhoneAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Phone model"""
    ordering = ['person']
    list_display = ('person', 'phone', 'type_phone')
    search_fields = ('person__firstname',)
    list_filter = ('type_phone',)


class ProductAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Product model"""
    ordering = ['product']
    list_display = (
        'ncm', 'imported', 'product', 'category', 'brand', 'cost', 'stock', 'outofline')
    date_hierarchy = 'created_at'
    search_fields = ('product', 'ncm')
    list_filter = ('imported', 'outofline', 'category', 'brand',)

admin.site.register(Person, PersonAdmin)  # Use the customized options
admin.site.register(Occupation)
admin.site.register(Address, AddressAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
