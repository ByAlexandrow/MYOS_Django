from django.urls import path

from . import views


app_name = 'victoria'

urlpatterns = [
    path('', views.victoria, name='victoria'),
]