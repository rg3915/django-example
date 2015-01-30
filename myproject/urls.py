from django.conf.urls import patterns, include, url
from myproject.core.views import *

from django.contrib import admin

urlpatterns = patterns(
    'myproject.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^persons/$', PersonList.as_view(), name='person_list'),
    url(r'^occupations/$', OccupationList.as_view(), name='occupation_list'),
    url(r'^persons/(?P<pk>\d+)/$',
        PersonDetail.as_view(), name='person_detail'),
    url(r'^products/$', ProductList.as_view(), name='product_list'),
    url(r'^brands/$', BrandList.as_view(), name='brand_list'),
    url(r'^categorys/$', CategoryList.as_view(), name='category_list'),

    url(r'^person/add/$', PersonCreate.as_view(), name='person_add'),
    url(r'^occupation/add/$', OccupationCreate.as_view(),
        name='occupation_add'),
    url(r'^address/add/$', AddressCreate.as_view(), name='address_add'),
    url(r'^phone/add/$', PhoneCreate.as_view(), name='phone_add'),
    url(r'^product/add/$', ProductCreate.as_view(), name='product_add'),
    url(r'^brand/add/$', BrandCreate.as_view(), name='brand_add'),
    url(r'^category/add/$', CategoryCreate.as_view(), name='category_add'),

    url(r'^download/$', 'download', name='download'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
