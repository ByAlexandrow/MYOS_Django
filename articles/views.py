from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from articles.models import Articles, ArticlesCategories


def all_categories(request, id):
    categories = ArticlesCategories.objects.filter(is_published=True)
    category = get_object_or_404(ArticlesCategories, pk=id)
    articles = Articles.objects.filter(category=category, is_published=True)
    paginator = Paginator(articles, 12)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'articles/all_categories.html', {'articles': articles, 'category': category, 'categories': categories})


def new_articles(request):
    news = Articles.objects.filter(is_published=True).order_by('-created_at')[:9]
    return render(request, 'articles/new_articles.html', {'news': news})


def article_detail(request, id):
    article = get_object_or_404(Articles, pk=id)
    return render(request, 'articles/article_detail.html', {'article': article})
