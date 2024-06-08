from django.db import models

from tinymce.models import HTMLField


class Victoria(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Наша история'
    )
    our_story = HTMLField(
        verbose_name='Вся наша история'
    )

    class Meta:
        verbose_name = 'Виктория'
        verbose_name_plural = 'Виктория'
