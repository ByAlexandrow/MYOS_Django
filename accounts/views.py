import random

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from articles.models import ArticlesCategories, Articles


@login_required
def profile(request, username):
    categories = categories = ArticlesCategories.objects.all()
    user = get_object_or_404(User, username=username)
    articles = list(Articles.objects.all())
    random_articles = random.sample(articles, min(4, len(articles)))
    return render(request, 'accounts/profile.html', {'user': user, 'categories': categories, 'random_articles': random_articles})
