from django.db import models



# Create your models here.
class Movie(models.Model):
    title =models.CharField(max_length=140)
    released_date=models.DateField()
    movie_time=models.CharField(max_length=100)
    movie_type=models.CharField(max_length=140)
    released_status=models.BooleanField(default=False)
    budget=models.IntegerField()
    revenue=models.IntegerField()
    video_trailer=models.FileField(upload_to='videos/%Y/%m/%d',null=True)
    movie_languages=models.TextField()
    tags=models.TextField()
    main_img=models.FileField(upload_to="images/%Y/%m/%d")
    overview=models.TextField(blank=True)
    img1=models.ImageField(upload_to="images/%Y/%m/%d",blank=True)
    img2=models.ImageField(upload_to="images/%Y/%m/%d",blank=True)
    img3=models.ImageField(upload_to="images/%Y/%m/%d",blank=True)
    img4=models.ImageField(upload_to="images/%Y/%m/%d",blank=True)
    img5=models.ImageField(upload_to="images/%Y/%m/%d",blank=True)
    user_watched=models.IntegerField()
    
    def __str__(self) :
        return self.title