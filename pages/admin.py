from django.contrib import admin
from django.http import HttpResponse
from .models import Movie
# Register your models here.
admin.site.register(Movie)