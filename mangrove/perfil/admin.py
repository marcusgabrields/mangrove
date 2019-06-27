from django.contrib import admin
from django.utils.html import mark_safe

from .models import Perfil


class PerfilModelAdmin(admin.ModelAdmin):

    list_display = ['name', 'title', 'photo_img']
    prepopulated_fields = {'slug': ('name',)}

    def photo_img(self, obj):
        return mark_safe('<img width="32px" src="/media/{}" />'
                         .format(obj.photo))

    photo_img.allow_tags = True
    photo_img.short_description = 'photo'


admin.site.register(Perfil, PerfilModelAdmin)
