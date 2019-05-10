from datetime import date
from django.test import TestCase

from blog.models import Article


class ArticleTest(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title='Meu titulo',
            slug='meu-titulo',
            content='Conteudo',
            preview='Previa',
            date=date.today(),
            draft=True
        )

    def test_can_create_a_article(self):
        self.assertTrue(Article.objects.exists())

    def test_article_fields(self):
        """Article must have [slug, title, content, preview, date, draft]"""
        fields = ['slug', 'title', 'content', 'preview', 'date', 'draft']

        for field in fields:
            with self.subTest():
                field_name = Article._meta.get_field(field).name
                self.assertEqual(field, field_name)

    def test_date_field_must_be_black_true(self):
        self.assertTrue(Article._meta.get_field('date').blank)

    def test_date_field_must_be_null_true(self):
        self.assertTrue(Article._meta.get_field('date').null)

    def test_preview_field_must_be_black_true(self):
        self.assertTrue(Article._meta.get_field('preview').blank)

    def test_content_field_must_be_black_true(self):
        self.assertTrue(Article._meta.get_field('content').blank)

    def test_draft_field_must_be_default_true(self):
        self.assertTrue(Article._meta.get_field('draft').default)

    def test(self):
        self.fail('Incluir perfil no Post')
