from django.urls import path

from . import views


app_name = 'articles'

urlpatterns = [
    path('all_categories/', views.all_categories, name='all_categories'),
    path('all_articles/', views.all_articles, name='all_articles'),
    path('new_articles/', views.new_articles, name='new_articles'),
    path('article/<int:id>/', views.article, name='article'),
]
