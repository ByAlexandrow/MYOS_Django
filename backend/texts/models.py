from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from tinymce.models import HTMLField
from colorfield.fields import ColorField
from Mystery_Of_Story.constants import (
    CHAR_FIELD_MAX_LENGTH, COLOR_FIELD_MAX_LENGTH
)


User = get_user_model()


class TextsGenres(models.Model):
    texts_genre = models.CharField(
        'Жанр',
        unique=True,
        max_length=CHAR_FIELD_MAX_LENGTH,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.texts_genre


class TextsCategoriesTags(models.Model):
    categories_title = models.CharField(
        max_length=20,
        verbose_name='Категория',
    )
    color = ColorField(
        'Цвет в НЕХ',
        unique=True,
        max_length=COLOR_FIELD_MAX_LENGTH
    )
    slug = models.SlugField(
        'Уникальный слаг',
        unique=True,
        max_length=CHAR_FIELD_MAX_LENGTH,
        default='',
    )
    publication = models.BooleanField(
        verbose_name='Опубликовать',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.categories_title


class Reactions(models.Model):
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


class Texts(models.Model):
    text_title = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    title_texts_img = models.ImageField(
        upload_to='image/texts_img/',
        verbose_name='Титульная картинка',
    )
    texts_description = HTMLField(
        default='Добавьте описание к вашему тексту!',
        verbose_name='Описание',
    )
    text = HTMLField(
        default='Пишите и редактируйте текст здесь!',
        verbose_name='Текст',
    )
    genre = models.ForeignKey(
        TextsGenres,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Жанр'
    )
    categories = models.ForeignKey(
        TextsCategoriesTags,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Категория'
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
    reactions = models.ForeignKey(
        Reactions,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Реакции',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать'
    )

    def __str__(self):
        return self.text_title
    
    def like(self, user):
        Reactions.objects.update_or_create(
            user=user,
            content_object=self,
            defaults={'reaction': Reactions.LIKE}
        )
    
    def likes(self):
        return self.reaction_set.filter(reaction=Reactions.LIKE).count()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'


class Comment(models.Model):
    comments_text = models.TextField('Текст комментария')
    comments = models.ForeignKey(
        Texts,
        on_delete=models.CASCADE,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='Уникальные подписки'
            )
        ]
    
    def clean(self):
        if self.user == self.following:
            raise ValidationError('Вы не можете подписаться на самого себя!')
    
    def __str__(self):
        return f'Подписка {self.user} на {self.following}'


class AbstractModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.ForeignKey(
        Texts,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True

    def clean(self):
        if self.__class__.objects.filter(
            user=self.user, text=self.text
        ).exists():
            raise ValidationError('Такая запись уже существует!')


class Favorites(AbstractModel):
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        default_related_name = 'favorites'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'text'],
                name='Уникальность избранного'
            )
        ]

    def __str__(self):
        return f'{self.user} добавил рецепт {self.text} в избранное!'
