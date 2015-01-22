from django.test import TestCase
from django.core.urlresolvers import reverse as r


class PersonListTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('person_list'))

    def test_get(self):
        'GET /persons/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'core/person/person_list.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '</th>', 6)


class OccupationListTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('occupation_list'))

    def test_get(self):
        'GET /occupations/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'core/person/occupation_list.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '</th>', 1)
