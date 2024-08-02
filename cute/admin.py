from django.contrib import admin

from cute.models import MyCuteAngel, AngelsImage


class AngelsImageInline(admin.StackedInline):
    model = AngelsImage
    extra = 1


@admin.register(MyCuteAngel)
class MyCuteAngelAdmin(admin.ModelAdmin):
    list_display = (
        'title_day', 'period', 'is_published'
    )
    list_filter = ('period',)
    inlines = [AngelsImageInline]
