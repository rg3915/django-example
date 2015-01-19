from django.conf.urls import patterns, include, url
from myproject.core.views import *

from django.contrib import admin

urlpatterns = patterns(
    'myproject.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^persons/$', PersonList.as_view(), name='person_list'),
    # url(r'^persons/(?P<pk>\d+)/$', 'person_detail', name='person_detail'),
    url(r'^products/$', ProductList.as_view(), name='product_list'),

    url(r'^person/add/$', PersonForm.as_view(), name='person_form'),
    url(r'^occupation/add/$', OccupationForm.as_view(),
        name='occupation_form'),
    url(r'^address/add/$', AddressForm.as_view(), name='address_form'),
    url(r'^phone/add/$', PhoneForm.as_view(), name='phone_form'),
    url(r'^product/add/$', ProductForm.as_view(), name='product_form'),
    url(r'^brand/add/$', BrandForm.as_view(), name='brand_form'),
    url(r'^category/add/$', CategoryForm.as_view(), name='category_form'),

    url(r'^download/$', 'download', name='download'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
