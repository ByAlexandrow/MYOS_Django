from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from articles.models import Articles, ArticlesCategories, ArticlesSubcategories


def all_categories(request, id):
    subcategories = ArticlesSubcategories.objects.filter(is_published=True)
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
    return render(request, 'articles/all_categories.html', {
        'articles': articles,
        'category': category,
        'categories': categories,
        'subcategories': subcategories
        })


def new_articles(request):
    all_articles = Articles.objects.filter(is_published=True).order_by('-created_at')
    filtered_articles = []
    for article in all_articles:
        if article.category and not article.category.is_published:
            continue
        if article.subcategory and not article.subcategory.is_published:
            continue
        filtered_articles.append(article)
    
    # Ограничиваем количество отображаемых статей до 9
    news = filtered_articles[:9]
    return render(request, 'articles/new_articles.html', {'news': news})


def article_detail(request, id):
    article = get_object_or_404(Articles, pk=id)
    return render(request, 'articles/article_detail.html', {'article': article})


def myths(request):
    category = get_object_or_404(ArticlesCategories, pk=2)
    subcategories = ArticlesSubcategories.objects.filter(category=category, is_published=True)
    return render(request, 'articles/myths.html', {'subcategories': subcategories})


def all_myths_in_sub(request, id):
    subcategories = ArticlesSubcategories.objects.filter(is_published=True)
    subcategory = get_object_or_404(ArticlesSubcategories, pk=id)
    articles = Articles.objects.filter(subcategory=subcategory, is_published=True).order_by('created_at')
    return render(request, 'articles/all_myths_in_sub.html', {'articles': articles, 'subcategories': subcategories, 'subcategory': subcategory})
