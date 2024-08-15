from django.db import models


class Achievements(models.Model):
    achieves_title = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    achieves_img = models.ImageField(
        upload_to='image/achieves/',
        verbose_name='Картинка достижения'
    )
    achieves_description = models.CharField(
        max_length=150,
        verbose_name='Описание достижения'
    )
    achieves_filter = models.CharField(
        max_length=50,
        verbose_name='Фильтр'
    )
    created_at = models.DateTimeField(
        verbose_name='Создано'
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовать'
    )

    def __str__(self):
        return self.achieves_title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'
