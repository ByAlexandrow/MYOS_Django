from django.shortcuts import render

from articles.models import ArticlesCategories


def index(request):
    categories = ArticlesCategories.objects.all()
    return render(request, 'homepage/index.html', {'categories': categories})
