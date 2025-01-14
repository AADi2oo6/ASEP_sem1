from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class destinations(models.Model):
    dest_name=models.CharField(max_length=100)
    dest_desc=models.TextField()
    dest_image=models.FileField(upload_to="Destinations/",max_length=250,null = True,default=None)
    dest_slug = AutoSlugField(populate_from ="dest_name", unique = True, null = True,default = None)


