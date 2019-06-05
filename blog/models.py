from django.db import models

from common.models import IndexedTimeStampedModel


class Article(IndexedTimeStampedModel):

    title = models.CharField('título', max_length=100)
    slug = models.SlugField()
    content = models.TextField('conteudo', blank=True)
    preview = models.TextField('prévia', blank=True)
    date = models.DateField('data', blank=True, null=True)
    author = models.ForeignKey('perfil.Perfil', on_delete=models.CASCADE)
    draft = models.BooleanField(default=True)
