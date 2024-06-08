from django.db import models
from django.contrib.auth.models import User

class AdminMessage(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages_to_admin'
    )
    subject = models.CharField(
        max_length=500,
        verbose_name='Суть письма'
    )
    message = models.TextField(
        verbose_name='Текст письма'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Временные данные',
    )

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Письмо для админа'
        verbose_name_plural = 'Письма для админа'

    def __str__(self):
        return f'Письмо от {self.user.username} на {self.timestamp}'
