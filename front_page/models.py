from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add=True,auto_now=False , null = True)
    modified = models.DateTimeField(auto_now=True,auto_now_add=False, null = True)
    description = models.TextField(max_length = 1000)
    content = RichTextField()
    author = models.ForeignKey('Author')
    catagory = models.ForeignKey('Catagory', null=True)
    
    class Meta:
        ordering = ['title']
        
    def __unicode__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length =50)
    
    def __unicode__(self):
        return self.name
    
class Catagory(models.Model):
    name = models.CharField(max_length =50)
    
    def __unicode__(self):
        return self.name