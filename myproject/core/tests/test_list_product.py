from django.test import TestCase
from django.core.urlresolvers import reverse as r


class ProductListTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('product_list'))

    def test_get(self):
        'GET /products/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'core/product/product_list.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '</th>', 8)


class BrandListTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('brand_list'))

    def test_get(self):
        'GET /brands/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'core/product/brand_list.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '</th>', 1)


class CategoryListTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('category_list'))

    def test_get(self):
        'GET /categorys/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(
            self.resp, 'core/product/category_list.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '</th>', 1)
