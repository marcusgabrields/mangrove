from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin

from .models import Article, Tag


@admin.register(Article)
class ArticleModelAdmin(MarkdownxModelAdmin):

    list_display = ['title', 'author', 'date', 'draft']
    prepopulated_fields = {'slug': ('title',)}


class TagModelAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, TagModelAdmin)
