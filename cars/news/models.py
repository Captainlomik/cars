from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=30, help_text="news title")
    content = models.TextField(max_length=1000)
    news_date = models.DateField(auto_now=True)
    publish = models.BooleanField('Опубликовать', default=False)

    def __str__(self):
        return self.title

    def make_published(modeleAdmin, request, queryset):
        queryset.update(publish=True)
    make_published.short_description="Опубликовать"