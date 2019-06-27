from django.test import TestCase

from mangrove.blog.models import Tag


class TagModelTest(TestCase):

    def test_can_create_a_tag(self):
        tag = Tag.objects.create(
            name='Python',
            slug='python'
        )

        self.assertTrue(Tag.objects.exists())