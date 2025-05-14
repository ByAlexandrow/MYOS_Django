import pytest

from articles.models import ArticlesCategories


@pytest.mark.django_db
def test_category_creaation(category):
    assert isinstance(category, ArticlesCategories)
    assert category.articles_category_title == 'Test Category'
    assert category.is_published is True


@pytest.mark.django_db
def test_category_str(category):
    assert str(category) == category.articles_category_title
