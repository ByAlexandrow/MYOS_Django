from django.shortcuts import render


def index(request):
    template = 'articles/index.html'
    return render(request, template)


def all_articles(request):
    template = 'articles/all_articles.html'
    return render(request, template)


def new_articles(request):
    template = 'articles/new_articles.html'
    return render(request, template)
