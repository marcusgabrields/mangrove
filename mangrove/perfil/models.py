from django.db import models


class Perfil(models.Model):

    name = models.CharField(max_length=255)
    title = models.TextField()
    resume = models.TextField()
    photo = models.ImageField()
