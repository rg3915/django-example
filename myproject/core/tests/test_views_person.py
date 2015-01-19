from django.test import TestCase
# from myproject.core.forms import PersonForm, ProductForm
from myproject.core.models import Person, Address, Product
from django.core.urlresolvers import reverse as r


class PersonTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('person_form'))

    def test_get(self):
        'GET /person/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp, 'core/person/person_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 9)
        self.assertContains(self.resp, 'type="text"', 5)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    # Não precisa deste teste em CreateView?
    # def test_has_form(self):
    #     'Context must have the person form.'
    #     form = self.resp.context['form']
    #     self.assertIsInstance(form, PersonForm)

# class SubscribePostTest(TestCase):
# 	def setUp(self):
# 		data = dict(
# 			name='Regis da Silva',
# 			cpf='00000000000',
# 			email='regis.santos.100@gmail.com',
# 			phone='11-00000000'
# 		)
# 		self.resp = self.client.post(r('subscriptions:subscribe'), data)

# 	def test_post(self):
# 		'Valid POST should redirect to /inscricao/1/'
# 		self.assertEqual(302, self.resp.status_code)

# 	def test_save(self):
# 		'Valid POST must be saved.'
# 		self.assertTrue(Subscription.objects.exists())

# class SubscribeInvalidPostTest(TestCase):
# 	def setUp(self):
# 		data = dict(
# 			name='Regis da Silva',
# cpf='000000000012', # 12 digitos
# 			email='regis.santos.100@gmail.com',
# 			phone='11-00000000'
# 		)
# 		self.resp = self.client.post(r('subscriptions:subscribe'), data)

# 	def test_post(self):
# 		'Invalid POST should not redirect.'
# 		self.assertEqual(200, self.resp.status_code)

# 	def test_form_errors(self):
# 		'Form must contain errors.'
# 		self.assertTrue(self.resp.context['form'].errors)

# 	def test_dont_save(self):
# 		'Do not save data.'
# 		self.assertFalse(Subscription.objects.exists())

# class TemplateRegressionTest(TestCase):
# 	def test_template_has_non_field_errors(self):
# 		'Check if non_field_errors are shown in template.'
# 		invalid_data = dict(name='Regis da Silva', cpf='00000000000')
# 		response = self.client.post(r('subscriptions:subscribe'), invalid_data)

# 		self.assertContains(response, '<ul class="errorlist">')


class OccupationTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('occupation_form'))

    def test_get(self):
        'GET /occupation/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp, 'core/person/occupation_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 2)
        self.assertContains(self.resp, 'type="text"', 1)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class AddressTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('address_form'))

    def test_get(self):
        'GET /address/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp, 'core/person/address_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 5)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class PhoneTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('phone_form'))

    def test_get(self):
        'GET /phone/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp, 'core/person/phone_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 2)
        self.assertContains(self.resp, 'type="text"', 1)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


# class MenuTest(TestCase):

#     def setUp(self):
#         self.resp = self.client.get(r('home'))

#     def test_get(self):
#         'GET /home/ must return status code 200.'
#         self.assertEqual(200, self.resp.status_code)

#     def test_template(self):
#         'Response should be a rendered template.'
#         self.assertTemplateUsed(self.resp, 'menu.html')

#     def test_html(self):
#         'Html must contain input controls.'
#         self.assertContains(self.resp, '"href"', 5)

class ProductTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('product_form'))

    def test_get(self):
        'GET /product/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp, 'core/product/product_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 10)
        self.assertContains(self.resp, 'type="text"', 2)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class BrandTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('brand_form'))

    def test_get(self):
        'GET /brand/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp, 'core/product/brand_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 2)
        self.assertContains(self.resp, 'type="text"', 1)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class CategoryTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('category_form'))

    def test_get(self):
        'GET /category/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp, 'core/product/category_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 2)
        self.assertContains(self.resp, 'type="text"', 1)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


# TODO person_list
