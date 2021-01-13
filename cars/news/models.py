from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=30, help_text="news title")
    content = models.TextField(max_length=1000)
    news_date = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.title
