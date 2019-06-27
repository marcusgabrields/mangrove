from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files import File
from model_mommy import mommy

from unittest import mock
import os

from mangrove.perfil.models import Perfil


User = get_user_model()

class PerfilTest(TestCase):

    def setUp(self):
        mocked_image = mock.MagicMock(spec=File)
        mocked_image.name = 'perfil_photo_test.png'

        self.p = Perfil.objects.create(
            name='Marcus Gabriel',
            title='Title',
            resume='Resume',
            photo=mocked_image
        )
        self.p.user = mommy.make(User)

        self.p.save()

    def tearDown(self):
        os.remove('perfil_photo_test.png')

    def test_can_create(self):
        self.assertTrue(Perfil.objects.exists())
