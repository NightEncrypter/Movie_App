import imp
from django.db import models
from pages.models import Movie
from django.contrib.auth.models import User
# Create your models here.
class Watchlist(models.Model):
    
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.movie