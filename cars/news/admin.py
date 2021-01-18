from django.contrib import admin
from .models import News, CommentNews


# Register your models here.

def make_published(modeleAdmin, request, queryset):
    queryset.update(publish=True)


make_published.short_description = "Опубликовать"

def make_Unpublished(modeleAdmin, request, queryset):
        queryset.update(publish=False)
make_Unpublished.short_description="Черновик"

# admin.site.register(News)


class NewsAdmin(admin.ModelAdmin):
    list_filter = ('publish', 'news_date')
    list_display = ('title', 'news_date', 'publish')
    
    actions = [make_published, make_Unpublished]
    


admin.site.register(News, NewsAdmin)

@admin.register(CommentNews)
class CommentNews(admin.ModelAdmin):
    list_display=('user', 'comment', 'date')

