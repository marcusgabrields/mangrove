from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .managers import UserManager
from mangrove.common.models import IndexedTimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):

    email = models.EmailField(
        _('email adress'),
        max_length=255,
        unique=True)

    is_trusty = models.BooleanField(
        _('trusty'),
        default=False,
        help_text=_('Designates whether this user has confirmed his account.'))

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log'
                    'into this admin site.')
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this user should be treated '
                    'as active. Unselect this instead of deleting accounts.')
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
