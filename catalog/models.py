from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth import get_user_model

User=get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    detail = models.TextField()
    
    image=models.ImageField(upload_to='images',default='images/images_2.png')

    def __str__(self):
        return self.title
    
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
    
    def __str__(self) :
        return self.first_name
    
    
        

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    
    
    def __str__(self) :
        return self.name
    
class Product(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    detail = models.TextField()
    
    image=models.ImageField(upload_to='images',default='images/images_2.png')
    
    
    def __str__(self) :
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail",kwargs={"pk":self.pk})
        # return "/detail/%s/" %(self.pk)
        
   
