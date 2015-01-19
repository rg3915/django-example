from django.contrib import admin
from .models import Person, Occupation, Address, Phone, Brand, Category, Product


class MyAdmin(admin.ModelAdmin):
    change_form_template = 'about.html'

    def get_osm_info(self):
        # ...
        pass

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['osm_data'] = self.get_osm_info()
        return super(MyAdmin, self).change_view(request, object_id,
                                                form_url, extra_context=extra_context)


class PersonAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Person model"""
    ordering = ['firstname']
    list_display = (
        '__str__', 'cpf', 'email', 'phone', 'occupation', 'created_at', 'active', 'blocked')
    date_hierarchy = 'created_at'
    search_fields = ('firstname', 'lastname')


class ProductAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Product model"""
    ordering = ['product']
    list_display = (
        'product', 'imported', 'ncm', 'category', 'brand', 'cost', 'stock')
    date_hierarchy = 'created_at'
    search_fields = ('product', 'ncm')
    list_filter = ('imported', 'category', 'brand',)

admin.site.register(Person, PersonAdmin)  # Use the customized options
admin.site.register(Occupation)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
