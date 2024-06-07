from django.contrib import admin

from texts.models import (
    TextsGenresTags, TextsCategories,
    Texts, Favorites, Follow, Reactions
)


@admin.register(TextsGenresTags)
class TagAdmin(admin.ModelAdmin):
    list_display = ('texts_tag', 'color', 'slug')


@admin.register(TextsCategories)
class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('categories_title',)


@admin.register(Texts)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'text_title', 'title_texts_img', 'texts_description',
        'text', 'genre', 'categories', 'author'
    )
    list_filter = ('text_title', 'author',)
    # filter_horizontal = ('tags',)

    def favorites(self, obj):
        return obj.favorites.count()


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'text')


@admin.register(Reactions)
class ReactionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'reaction')

