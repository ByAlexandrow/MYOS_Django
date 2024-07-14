from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from tinymce.models import HTMLField


User = get_user_model()


class ArticlesCategories(models.Model):
    articles_category_title = models.CharField(
        max_length=40,
        verbose_name='Категория',
    )
    articles_category_img = models.ImageField(
        upload_to='image/articles_category/',
        verbose_name='Титульная картинка категории',
    )
    articles_category_description = models.CharField(
        max_length=100,
        verbose_name='Описание',
        default='Описание категории',
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовать',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.articles_category_title


class ArticlesReactions(models.Model):
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'
    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    ]

    reaction = models.CharField(
        max_length=7,
        choices=REACTION_CHOICES,
    )

    class Meta:
        verbose_name = 'Реакция'
        verbose_name_plural = 'Реакции'
    
    def __str__(self):
        return self.reaction


class Articles(models.Model):
    articles_title = models.CharField(
        max_length=30,
        verbose_name='Название статьи',
    )
    articles_title_img = models.ImageField(
        upload_to='image/articles_img/',
        verbose_name='Титульная картинка',
    )
    articles_description = models.CharField(
        max_length=50,
        default='Описание статьи для титульной страницы!',
        verbose_name='Описание статьи',
    )
    articles_text = models.TextField(
        default='Здесь надо добавить текст статьи!',
        verbose_name='Текст статьи',
    )
    reactions = models.ManyToManyField(
        ArticlesReactions,
        blank=True,
        verbose_name='Реакции',
    )
    category = models.ForeignKey(
        ArticlesCategories,
        on_delete=models.CASCADE,
        null=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Автор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать'
    )

    def __str__(self):
        return self.articles_title
    
    def like(self, user):
        ArticlesReactions.objects.update_or_create(
            user=user,
            content_object=self,
            defaults={'reaction': ArticlesReactions.LIKE}
        )
    
    def likes(self):
        return self.reaction_set.filter(reaction=ArticlesReactions.LIKE).count()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticlesComment(models.Model):
    comments_text = models.TextField('Текст комментария')
    comments = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class AbstractModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True

    def clean(self):
        if self.__class__.objects.filter(
            user=self.user, article=self.article
        ).exists():
            raise ValidationError('Запись уже существует!')


class ArticlesFavorites(AbstractModel):
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        default_related_name = 'articles_favorites'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'article'],
                name='Уникальность в избранном'
            )
        ]

    def __str__(self):
        return f'Вы добавили статью {self.article} в избранное!'
