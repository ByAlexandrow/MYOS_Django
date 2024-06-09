from django.urls import include, path
from rest_framework import routers

from api.views import (
    UserViewSet, # CategoryTagViewSet, TextViewSet,
    # GenreViewSet, ArticleViewSet,
)

app_name = 'api'

router_v1 = routers.DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')
# router_v1.register('category', CategoryTagViewSet, basename='category')
# router_v1.register('text', TextViewSet, basename='text')
# router_v1.register('genre', GenreViewSet, basename='genre')
# router_v1.register('article', ArticleViewSet, basename='article')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
