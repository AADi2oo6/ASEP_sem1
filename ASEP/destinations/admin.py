from django.contrib import admin
from destinations.models import destinations

# Register your models here.

class destinationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'dest_name','dest_category','dest_desc',"news_description",'lat','long','dest_slug']
admin.site.register(destinations,destinationsAdmin)
