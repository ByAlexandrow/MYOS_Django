from django.contrib import admin

from users.models import AdminMessage


@admin.register(AdminMessage)
class MessageForAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'timestamp',)
    list_filter = ('user', 'subject', 'timestamp',)
