# blog/models.py

from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    
class post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    status = models.BooleanField(default=True)
    
    
    def __str__(self) :
        return self.title[:50]