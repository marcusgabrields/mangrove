from django.db import models
from django.utils.translation import ugettext_lazy as _
from markdownx.models import MarkdownxField

from mangrove.common.models import IndexedTimeStampedModel


class Tag(IndexedTimeStampedModel):

    name = models.CharField(_('name'), max_length=15)
    slug = models.SlugField(_('slug'), unique=True)

    def __str__(self):
        return self.name


class Article(IndexedTimeStampedModel):

    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    content = MarkdownxField(_('content'), blank=True)
    preview = models.TextField(_('preview'), blank=True)
    date = models.DateField(_('date'), blank=True, null=True)
    author = models.ForeignKey('perfil.Perfil', verbose_name=_('author'),
                               on_delete=models.CASCADE)
    tags = models.ManyToManyField('blog.Tag')
    draft = models.BooleanField(_('draft'), default=True)

    def __str__(self):
        return self.title
