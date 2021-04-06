from django.db import models

# Create your models here.

# class Author(models.Model):
#       picture = models.ImageField(upload_to='gallery', blank=True, null=True) 

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'posts_image')

    def __str__(self):
        return self.title 
