from django.contrib import admin

from articles.models import (
    Articles, ArticlesCategories, ArticlesImage, ArticlesSubcategories
)

class ArticlesImageInline(admin.StackedInline):
    model = ArticlesImage
    extra = 1


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = (
        'articles_title', 'category', 'author',
        'created_at', 'is_published'
    )
    list_display_links = ('articles_title', 'category',)
    list_filter = ('category',)
    inlines = [ArticlesImageInline]


@admin.register(ArticlesCategories)
class ArticlesCategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'articles_category_title', 'articles_category_description',
        'created_at', 'is_published'
    )
    list_display_links = ('articles_category_title',)
    list_filter = ('articles_category_title',)


@admin.register(ArticlesSubcategories)
class ArticlesSubcategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'articles_subcategory_title', 'articles_subcategory_description',
        'category', 'created_at', 'is_published'
    )
    list_display_links = ('articles_subcategory_title',)
    list_filter = ('articles_subcategory_title',)
