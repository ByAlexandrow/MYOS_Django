from django.shortcuts import render, get_object_or_404

from articles.models import Articles, ArticlesCategories


def all_categories(request, slug):
    category = get_object_or_404(ArticlesCategories, slug=slug)
    articles = Articles.objects.filter(category=category).order_by('-created_at')
    return render(request, 'articles/all_categories.html', {'category': category, 'articles': articles})


def article(request, id):
    article = get_object_or_404(Articles, id=id)
    return render(request, 'articles/article.html', {'article': article})


def new_articles(request):
    news = Articles.objects.all().order_by('-created_at')[:9]
    return render(request, 'articles/new_articles.html', {'news': news})
