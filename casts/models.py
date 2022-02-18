from pickle import TRUE
from django.db import models

from pages.models import Movie
# Create your models here.
class Cast(models.Model):
    cast_name=models.CharField(max_length=100)
    cast_age=models.IntegerField()
    cast_movie_name=models.CharField(max_length=150)
    movie=models.ForeignKey(Movie,  on_delete=models.CASCADE)
    cast_img=models.ImageField(upload_to="images/%Y/%m/%d",blank=True)
    
    
    def __str__(self):
        return f"{self.cast_name} ==> {self.movie}"