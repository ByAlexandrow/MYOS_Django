from django.urls import path

from . import views


app_name = 'piligrimka'

urlpatterns = [
    path('', views.piligrimka, name='piligrimka'),
]