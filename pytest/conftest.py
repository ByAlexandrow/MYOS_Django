import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from articles.models import ArticlesCategories, ArticlesSubcategories, Articles, ArticlesImage


User = get_user_model()

@pytest.fixture
def user(db):
    return User.objects.create_user(
        username='Test User',
        email='email@mail.ru',
        password='1234567890'
    )


@pytest.fixture
def category(db):
    return ArticlesCategories.objects.create(
        articles_category_title='Test Category',
        articles_category_img='path/to/the/category_img.png',
        articles_category_description='Test description',
        is_published=True
    )


@pytest.fixture
def subcategory(db, category):
    return ArticlesSubcategories.objects.create(
        articles_subcategory_title='Test Subcategory',
        articles_subcategory_img='path/to/the/subcategory_img.png',
        articles_subcategory_description='Test description',
        category=category,
        is_published=True
    )


@pytest.fixture
def article(db, user, category, subcategory):
    return Articles.objects.create(
        articles_title='Test Article',
        articles_title_img='path/to/the/article_img.png',
        articles_description='Test description',
        category=category,
        subcategory=subcategory,
        author=user,
        is_published=True
    )


@pytest.fixture
def carousel(db, article):
    return ArticlesImage.objects.create(
        about_us=article,
        images='path/to/the/carousel_img.png' 
    )
