from django.db import models

from tinymce.models import HTMLField


class Piligrimka(models.Model):
    best_img = models.ImageField(
        upload_to='images/moments/',
        verbose_name='Фото дня'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название момента'
    )
    our_story = HTMLField(
        verbose_name='Вся наша история'
    )
    period = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Период',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Пилигримка'
        verbose_name_plural = 'Пилигримка'

    def __str__(self):
        return self.title