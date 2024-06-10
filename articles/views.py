from django.shortcuts import render


def index(request):
    template = 'articles/index.html'
    return render(request, template)
