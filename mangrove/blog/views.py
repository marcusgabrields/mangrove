from django.shortcuts import get_object_or_404, render

from mangrove.blog.models import Article, Tag


def blog(request):
    context = {
        'articles': Article.finisheds.all(),
        'categories': Tag.objects.all(),
    }
    return render(request, 'blog/blog.html', context)


def article(request, slug):
    context = {
        'article': get_object_or_404(Article.finisheds, slug=slug)
    }
    return render(request, 'blog/article.html', context)
