import pytest

from articles.models import ArticlesImage


@pytest.mark.django_db
def test_carousel_creation(carousel, article):
    assert isinstance(carousel, ArticlesImage)
    assert carousel.about_us == article
    assert carousel.images == 'path/to/the/carousel_img.png'


@pytest.mark.django_db
def test_carousel_str(carousel):
    assert str(carousel) == carousel.images
