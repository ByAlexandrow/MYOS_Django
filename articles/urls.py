from django.urls import path

from . import views


app_name = 'articles'

urlpatterns = [
    path('all_categories/<int:id>/', views.all_categories, name='all_categories'),
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
    path('new_articles/', views.new_articles, name='new_articles'),
    path('myths/', views.myths, name='myths'),
    path('all_myths_in_sub/<int:id>/', views.all_myths_in_sub, name='all_myths_in_sub')
]
