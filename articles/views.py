from django.shortcuts import render, get_object_or_404

from articles.models import Articles, ArticlesCategories


def all_categories(request):
    categories = ArticlesCategories.objects.all().order_by('-created_at')
    return render(request, 'articles/all_categories.html', {'categories': categories})


def all_articles(request):
    articles = Articles.objects.filter(category=1)
    return render(request, 'articles/all_articles.html', {'articles': articles})


def new_articles(request):
    newest = Articles.objects.all().order_by('-created_at')
    return render(request, 'articles/new_articles.html', {'newest': newest})


def article(request, id):
    article = get_object_or_404(Articles, id=id)
    return render(request, 'articles/article.html', {'article': article})
