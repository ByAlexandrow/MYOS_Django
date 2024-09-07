from django.shortcuts import render

from articles.models import Articles, ArticlesCategories


def index(request):
    categories = ArticlesCategories.objects.filter(is_published=True)
    new_articles = Articles.objects.filter(is_published=True).order_by('-created_at')[:3]
    return render(request, 'homepage/index.html', {'categories': categories, 'new_articles': new_articles})
