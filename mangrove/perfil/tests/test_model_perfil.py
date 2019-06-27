import os
from unittest import mock

from django.contrib.auth import get_user_model
from django.core.files import File
from django.test import TestCase
from model_mommy import mommy

from mangrove.perfil.models import Perfil


User = get_user_model()


class PerfilTest(TestCase):

    def setUp(self):
        mocked_image = mock.MagicMock(spec=File)
        mocked_image.name = 'perfil_photo_test.png'

        self.p = Perfil.objects.create(
            user=mommy.make(User),
            name='Marcus Gabriel',
            title='Title',
            resume='Resume',
            photo=mocked_image
        )

    def tearDown(self):
        os.remove('mediafiles/perfil_photo_test.png')

    def test_can_create(self):
        self.assertTrue(Perfil.objects.exists())
