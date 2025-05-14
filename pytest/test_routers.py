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
def test_category_page(client):
    url = reverse('articles:all_categories')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_legends_category_page(client, category):
    url = reverse('articles:all_categories')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_myths_category_page(client):
    url = reverse('articles:all_categories')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_wonders_category_page(client):
    url = reverse('articles:all_categories')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_inventions_category_page(client):
    url = reverse('articles:all_categories')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_people_category_page(client):
    url = reverse('articles:all_categories')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_404_page(client):
    response = client.get('/page-does-not-exist/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_403csrf_page(client):
    response = client.get('/page-does-not-exist/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_500_page(client):
    response = client.get('/page-does-not-exist/')
    assert response.status_code == 500
