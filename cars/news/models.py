from django.db import models
from django.contrib.auth.models import User

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

    def make_Unpublished(modeleAdmin, request, queryset):
        queryset.update(publish=False)
    make_Unpublished.short_description="Черновик"

class CommentNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000, null=True)
    date = models.DateField(auto_now=True)
    news=models.ForeignKey(News, on_delete=models.CASCADE)