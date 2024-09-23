from django.urls import path

from . import views


app_name = 'cute'

urlpatterns = [
    path('angel/', views.angel, name='angel'),
]
