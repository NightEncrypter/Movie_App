from tkinter import CASCADE
from django.db import models

from pages.models import Movie
from django.contrib.auth.models import User 
# from pages.models import Movie

# Create your models here.
class Review(models.Model):
    
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField(null=True)
    rating=models.IntegerField(null=True)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    
    def __str__(self):
        return "review"
