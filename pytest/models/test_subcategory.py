import pytest

from articles.models import ArticlesSubcategories


@pytest.mark.django_db
def test_subcategory_creaation(subcategory):
    assert isinstance(subcategory, ArticlesSubcategories)
    assert subcategory.articles_subcategory_title == 'Test Subcategory'
    assert subcategory.is_published is True


@pytest.mark.django_db
def test_subcategory_str(subcategory):
    assert str(subcategory) == subcategory.articles_subcategory_title
