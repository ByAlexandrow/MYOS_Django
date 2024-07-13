from django.shortcuts import render

from articles.models import Articles, ArticlesCategories


def index(request):
    categories = ArticlesCategories.objects.all()
    new_articles = Articles.objects.all().order_by('-created_at')[:3]
    return render(request, 'homepage/index.html', {'categories': categories, 'new_articles': new_articles})
