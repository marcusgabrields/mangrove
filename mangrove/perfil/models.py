from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name=_('user'))
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True)
    title = models.TextField(_('title'))
    resume = models.TextField(_('resume'))
    photo = models.ImageField(_('photo'), default='avatar/crab-avatar.png')

    def __str__(self):
        return self.name
