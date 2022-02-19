from django.contrib import admin
from django.http import HttpResponse
from .models import Movie

# Customize the admin 

# Register your models here.
# admin.site.register(Movie)


class MovieAdmin(admin.ModelAdmin):
    list_display=("id","title","overview","released_date")
    
    list_display_links=("id","title")
    search_fields=("title","overview")
    list_per_page=5
admin.site.register(Movie,MovieAdmin)
    