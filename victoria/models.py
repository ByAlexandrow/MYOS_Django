from django.db import models

from tinymce.models import HTMLField


class Victoria(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название момента'
    )
    our_story = HTMLField(
        verbose_name='Вся наша история'
    )
    period = models.CharField(
        max_length=50,
        default='',
        verbose_name='Период',
    )
    created_at = models.DateField(
        auto_now=True,
        verbose_name='Дата создания',
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Виктория'
        verbose_name_plural = 'Виктория'
