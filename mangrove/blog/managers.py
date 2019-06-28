from django.db import models


class FinishedsArticleManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(draft=False)