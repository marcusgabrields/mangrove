from django.shortcuts import render

from mangrove.blog.models import Article


def blog(request):
    context = {
        'article': Article.objects.first()
    }
    return render(request, 'blog/blog.html', context)
