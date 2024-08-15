from django.contrib import admin

from achievements.models import Achievements


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('achieves_title',)
    list_filter = ('achieves_filter',)
