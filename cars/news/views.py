from django.shortcuts import render
from rest_framework import viewsets

from .serializers import NewsSerializer
from .models import News

# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset=News.objects.all().order_by('title')
    serializer_class=NewsSerializer