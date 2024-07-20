from django.contrib import admin

from piligrimka.models import Piligrimka


@admin.register(Piligrimka)
class PiligrimkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'period')
    list_filter = ('period',)