from django.db import models
from django.utils.translation import ugettext_lazy as _
from markdownx.models import MarkdownxField
from django.urls import reverse

from mangrove.common.models import IndexedTimeStampedModel
from .managers import FinishedsArticleManager


class Tag(IndexedTimeStampedModel):

    name = models.CharField(_('name'), max_length=15)
    slug = models.SlugField(_('slug'), unique=True)

    def __str__(self):
        return self.name


class Article(IndexedTimeStampedModel):

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True, max_length=255)
    content = MarkdownxField(_('content'), blank=True)
    preview = models.TextField(_('preview'), blank=True)
    date = models.DateField(_('date'), blank=True, null=True)
    author = models.ForeignKey('perfil.Perfil', verbose_name=_('author'),
                               on_delete=models.CASCADE)
    tags = models.ManyToManyField('blog.Tag')
    draft = models.BooleanField(_('draft'), default=True)

    finisheds = FinishedsArticleManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug})
