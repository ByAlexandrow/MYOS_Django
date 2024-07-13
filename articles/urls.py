from django.urls import path

from . import views


app_name = 'articles'

urlpatterns = [
    path('category/<slug:slug>/', views.all_categories, name='all_categories'),
    path('article/<int:id>/', views.article, name='article'),
    path('new_articles/', views.new_articles, name='new_articles'),
]
