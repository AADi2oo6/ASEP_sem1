from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
# Create your models here.

class destinations(models.Model):
    dest_name=models.CharField(max_length=100)
    dest_category=models.CharField(max_length=100, default=None, null=True)
    dest_desc=models.TextField(default=None, null=True)
    news_description=HTMLField(default=None, null=True)
    lat=models.FloatField(default=None, null=True)
    long=models.FloatField(default=None, null=True)
    dest_image=models.FileField(upload_to="Destinations/",max_length=250,null = True,default=None)
    dest_image1=models.FileField(upload_to="Destinations/",max_length=250,null = True,default=None)
    dest_image2=models.FileField(upload_to="Destinations/",max_length=250,null = True,default=None)
    dest_image3=models.FileField(upload_to="Destinations/",max_length=250,null = True,default=None)
    dest_image4=models.FileField(upload_to="Destinations/",max_length=250,null = True,default=None)

    dest_slug = AutoSlugField(populate_from ="dest_name", unique = True, null = True,default = None)


class emergincy(models.Model):
    catagory=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    area = models.CharField(max_length=100)
    location = models.URLField()