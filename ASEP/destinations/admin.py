from django.contrib import admin
from destinations.models import destinations, emergincy

# Register your models here.

class destinationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'dest_name','dest_category','dest_desc',"news_description",'lat','long','dest_slug']
admin.site.register(destinations,destinationsAdmin)

class emergincyAdmin(admin.ModelAdmin):
    list_display = ['id', 'catagory','phone','email','address','area','location']
admin.site.register(emergincy,emergincyAdmin)