from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Person_information, Person_auto, Dock, Comment
# Register your models here.

@admin.register(Person_information)
class PersonInfo(admin.ModelAdmin):
    list_display = ('person', 'phone')
    search_fields = ['phone', 'adress']


"""class PersonAuto(admin.ModelAdmin):
    list_display = ('name', 'owner', 'price', 'kilometrage')
    StackedInline = [addDocks]
    """

@admin.register(Dock)
class Docks(admin.ModelAdmin):
    list_display = ('car',  'state_number')
    


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('user', 'date', 'comment')



class expPerson_auto(resources.ModelResource):
    
    class Meta:
        model = Person_auto

class addDocks(admin.TabularInline):
    model = Dock

class exportAd(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'owner', 'price', 'kilometrage')
    
    search_fields = ['name', 'price']
   
    resource_class = expPerson_auto
    
    inlines=[addDocks]

admin.site.register(Person_auto, exportAd)
