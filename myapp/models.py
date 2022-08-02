from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pydoc import describe
from turtle import title
from django.db import models

# Create your models here.


# create categories model 

class Category(models.Model):
    
    title = models.CharField(max_length=100)
    
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
#create Image model

class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images',max_length=200,null=True,default=None)
    added_date = models.DateTimeField()
    cat = models.ForeignKey(Category , on_delete=models.CASCADE) 
    
    
    def __str__(self):
        return self.title