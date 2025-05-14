import  pytest

from articles.models import Articles


@pytest.mark.django_db
def test_article_creaation(article):
    assert isinstance(article, Articles)
    assert article.articles_title == 'Test Article'
    assert article.is_published is True


@pytest.mark.django_db
def test_article_str(article):
    assert str(article) == article.articles_title
