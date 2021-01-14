from django.contrib import admin
from .models import  Person_information, Person_auto, Dock, Comment
# Register your models here.

@admin.register(Person_information)
class PersonInfo(admin.ModelAdmin):
    list_display=('person', 'phone')

@admin.register(Person_auto)
class PersonAuto(admin.ModelAdmin):
    list_display=('name', 'owner', 'price','kilometrage')

@admin.register(Dock)
class Docks(admin.ModelAdmin):
    list_display=('car',  'state_number')

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display=('user', 'date', 'comment')