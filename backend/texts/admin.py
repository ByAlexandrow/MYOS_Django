from django.contrib import admin

from texts.models import (
    TextsGenres, TextsCategoriesTags,
    Texts, Favorites, Follow, Reactions,
    Comment
)


@admin.register(TextsGenres)
class TextsGenreAdmin(admin.ModelAdmin):
    list_search = ('texts_genres',)
    list_display = ('texts_genre',)
    list_display_links = ('texts_genre',)
    list_filter = ('texts_genre',)


@admin.register(TextsCategoriesTags)
class TextsCategoriesTagsAdmin(admin.ModelAdmin):
    list_display = ('categories_title',)
    list_display_links = ('categories_title',)
    list_search = ('categories_title',)
    list_filter = ('categories_title', 'color', 'slug')


@admin.register(Texts)
class TextAdmin(admin.ModelAdmin):
    list_search = ('text_title', 'genre', 'categories', 'author')
    list_display = (
        'text_title', 'title_texts_img', 'texts_description',
        'text', 'genre', 'categories', 'author', 'is_published'
    )
    list_display_links = ('text_title',)
    list_editable = ('is_published',)
    list_filter = ('text_title', 'author', 'genre', 'categories',)

    def favorites(self, obj):
        return obj.favorites.count()
    
    def reactions(self, obj):
        return obj.reactions.count()


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    list_display_links = ('user',)


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'text')
    list_display_links = ('user', 'text')


@admin.register(Reactions)
class ReactionsAdmin(admin.ModelAdmin):
    list_search = ('reaction',)
    list_display = ('reaction',)
    list_filter = ('reaction',)

