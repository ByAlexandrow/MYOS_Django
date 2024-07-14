from django.urls import path

from . import views


app_name = 'articles'

urlpatterns = [
    path('all_categories/<int:id>/', views.all_categories, name='all_categories'),
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
    path('new_articles/', views.new_articles, name='new_articles'),
]
