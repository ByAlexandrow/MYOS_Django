from django.db import models

from tinymce.models import HTMLField
from PIL import Image, ImageOps


class MyCuteAngel(models.Model):
    title_day = models.CharField(
        max_length=40,
        verbose_name='Название дня',
    )
    day_description = HTMLField(
        default=(
            f'Текст статьи. 1 отступ. 100-130 слов. Шрифт: заголовки - 18, подзаголовки - 14, текст - 12, белый цвет.'
        ),
        verbose_name='Описание дня',
        blank=True,
    )
    period = models.CharField(
        max_length=30,
        verbose_name='Приод отношений',
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовать',
    )


    def __str__(self):
        return self.title_day


    class Meta:
        ordering = ['-date']
        verbose_name = 'Ангел'
        verbose_name_plural = 'Ангел'


class AngelsImage(models.Model):
    about_us = models.ForeignKey(
        MyCuteAngel,
        related_name='img',
        on_delete=models.CASCADE,
        verbose_name='Статья',
    )
    images = models.ImageField(
        upload_to='img/angels_carousel/',
        verbose_name='Карусель картинок',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.images.name}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.images:
            img = Image.open(self.images.path)
            target_width = 800
            target_height = int(target_width * 9 / 16)
            img = ImageOps.fit(img, (target_width, target_height), Image.Resampling.LANCZOS)
            img.save(self.images.path)
