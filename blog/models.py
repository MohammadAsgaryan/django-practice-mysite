from django.db import models

# Create your models here.
class Post(models.Model):
    # image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    content = models.TextField()
    #category = models.CharField(max_length=100)
    #tags = models.CharField(max_length=200)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    #author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title