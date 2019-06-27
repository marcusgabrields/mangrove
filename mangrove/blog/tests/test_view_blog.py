from django.test import TestCase
from django.shortcuts import resolve_url


class BlogViewTest(TestCase):

    def setUp(self):
        self.url = resolve_url('blog')
        self.resp = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'blog/blog.html')

    # def test_fail(self):
    #     self.fail('Quando o templateestiver pronto, integrar com o back')
