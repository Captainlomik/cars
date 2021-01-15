from django.contrib import admin
from .models import  Service_info, Service_auto, Order, Message
# Register your models here.

#admin.site.register(Company)
#admin.site.register(Service_info)
#admin.site.register(Service_auto)

#class CompanyAdmin(admin.ModelAdmin):
   # pass

#admin.site.register(Company, CompanyAdmin)

@admin.register(Service_info)
class ServiceInfoAdmin(admin.ModelAdmin):
    list_display=('name', 'location', 'phone', 'owner')


@admin.register(Service_auto)
class ServiceInfoAuto(admin.ModelAdmin):
    list_display=('name', 'price', 'service')
   # list_filter=('price')

   
@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('user', 'time_visit', 'phone')

@admin.register(Message)
class Message(admin.ModelAdmin):
    list_display = ('user', 'service', 'text')