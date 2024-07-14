from django.contrib import admin

from articles.models import (
    Articles, ArticlesCategories,
    ArticlesFavorites, ArticlesReactions
)


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = (
        'articles_title', 'articles_title_img',
        'category', 'author', 'created_at',
        'is_published'
    )
    list_display_links = ('articles_title', 'category',)
    list_filter = ('category',)


@admin.register(ArticlesCategories)
class ArticlesCategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'articles_category_title', 'articles_category_img',
        'created_at', 'is_published'
    )
    list_display_links = ('articles_category_title',)
    list_filter = ('articles_category_title',)


@admin.register(ArticlesFavorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'article')
    list_display_links = ('user', 'article')


@admin.register(ArticlesReactions)
class ReactionsAdmin(admin.ModelAdmin):
    list_search = ('reaction',)
    list_display = ('reaction',)
    list_filter = ('reaction',)
