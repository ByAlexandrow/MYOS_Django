from django.urls import path

from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_articles/', views.all_articles, name='all_articles'),
    path('new_articles/', views.new_articles, name='new_articles'),
]
