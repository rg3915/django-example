from django.test import TestCase
from django.core.urlresolvers import reverse as r


class PersonTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('person_add'))

    def test_get(self):
        'GET /person/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'core/person/person_create_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 8)
        self.assertContains(self.resp, 'type="text"', 4)
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


class OccupationTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('occupation_add'))

    def test_get(self):
        'GET /occupation/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'core/person/occupation_create_form.html')

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
        self.resp = self.client.get(r('address_add'))

    def test_get(self):
        'GET /address/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'core/person/address_create_form.html')

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
        self.resp = self.client.get(r('phone_add'))

    def test_get(self):
        'GET /phone/add/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'core/person/phone_create_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 2)
        self.assertContains(self.resp, 'type="text"', 1)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
