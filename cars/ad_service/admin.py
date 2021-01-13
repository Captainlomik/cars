from django.contrib import admin
from .models import Company, Service_info, Service_auto
# Register your models here.

#admin.site.register(Company)
#admin.site.register(Service_info)
#admin.site.register(Service_auto)

class CompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Company, CompanyAdmin)

@admin.register(Service_info)
class ServiceInfoAdmin(admin.ModelAdmin):
    list_display=('name', 'location', 'company', 'phone')


@admin.register(Service_auto)
class ServiceInfoAuto(admin.ModelAdmin):
    list_display=('name', 'price', 'service')
   # list_filter=('price')