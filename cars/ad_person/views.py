from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PersonAutoSerializer, DocksSerializer, UserSerializer
from .models import Person_auto, Dock
from django.contrib.auth.models import User

# Create your views here.


class PersonAutoViewSet(viewsets.ModelViewSet):
    queryset = Person_auto.objects.all()
    serializer_class = PersonAutoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DockSet(viewsets.ModelViewSet):
    queryset = Dock.objects.all()
    serializer_class = DocksSerializer