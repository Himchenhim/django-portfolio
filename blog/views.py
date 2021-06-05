from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Article


def all_blogs(request):
    articles = Article.objects.all()
    return render(request, 'blog/all_blogs.html', {'articles': articles})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/detail.html', {'article': article})
