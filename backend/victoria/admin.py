from django.contrib import admin

from victoria.models import Victoria


@admin.register(Victoria)
class VictoriaAdmin(admin.ModelAdmin):
    list_search = ('period',)
    list_display = ('title', 'our_story')
    list_filter = ('period',)
