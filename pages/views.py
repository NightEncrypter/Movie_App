from re import search
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from reviews.models import Review
from .models import Movie
from django.core.paginator import Paginator
from casts.models import Cast
# Create your views here.


def index(request):
    search=True
    ham=True
    login=True
    movielist=Movie.objects.order_by("-released_date")
    
    #? Search data
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    # ? - sign refer to descending order
    
    
    movielist=movielist.filter(Q(title__icontains=q)| Q(tags__icontains=q)| Q(movie_languages__icontains=q))
     
    print(movielist,"query")
    # ? - sign refer to descending order and filter method filter the data in specific way
    # movielist=Movie.objects.order_by("-released_date").filter(releassed=True)
    
    paginator=Paginator(movielist,2)
    
    
    
    
    
    #? For pagination-BUTTON
    page=request.GET.get("page")
    
    paged_listings=paginator.get_page(page)
    total_movies=paginator.count
    
    context={"ham":ham ,"search":search ,"movielist":paged_listings,"total_movies":total_movies,"login":login}
    
    # print(paged_listings.paginator)
    
    return render(request, "pages/index.html",context)


def about(request):
    return render(request, "pages/about.html")
# def login(request):
#     search=False
#     ham=False
#     context={"ham":ham ,"search":search}
#     return render(request,"pages/login.html",context)

# def register(request):
#     search=False
#     ham=False
#     context={"ham":ham  ,"search":search}
#     return render(request,"pages/register.html",context)

def movie(request,movie_id):
    
    login=True
    # print(request.user.is_authenticated,"user-authnticated")
    single_movie=get_object_or_404(Movie,pk=int(movie_id))
    
    casts=Cast.objects.filter(movie=movie_id)
    
    reviews=Review.objects.filter(movie_id=movie_id)
    
    print(reviews)
    
    # print(casts)
    
    tags=single_movie.tags.split(',')
    
    # print(tags,"split")
    
    # Get a related data
    related_movies=Movie.objects.filter(Q(title__icontains=single_movie.title)| Q(tags__icontains=single_movie.tags)| Q(movie_languages__icontains=single_movie.movie_languages))
    # print("related",related_movies)
    
    # print(single_movie)
    search=True
    context={"search":search ,"movie_data":single_movie,"casts":casts ,"related_movies":related_movies,"tags":tags,"reviews":reviews,"login":login}
    
    return render(request,"pages/movie.html",context)

def cat(request):
    login=True
    search=True
    # auth=False
    ham=True
    hollywood=Movie.objects.filter(Q(tags__icontains="hollywood")|Q(movie_type__icontains="hollywood"))
    
    # print(hollywood,"hollywood")
    context={"ham":ham ,"search":search,"hollywood":hollywood,"login":login
             }
    return render(request,"pages/categories.html",context)