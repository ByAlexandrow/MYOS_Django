import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_page(client):
    url = reverse('homepage:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_new_articles_page(client):
    url = reverse('articles:new_articles')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_404_page(client):
    response = client.get('/page-does-not-exist/')
    assert response.status_code == 404
