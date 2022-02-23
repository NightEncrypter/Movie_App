from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from pages.models import Movie
from .models import Watchlist

# Create your views here.


def watchlistData(request):
    
    
    getAllWatchlist=Watchlist.objects.filter(user_id=request.user.id)
    # print(get_all_watchlist)
    
    context={"watchlist":getAllWatchlist}
    
    # print(context)
    
    return render(request,"watchlist/index.html",context)



def addInWatchlist(request):
    # print(w_id)
    if request.user.is_authenticated:
        
        if request.method=="POST":
            # request.POST
            print(request.POST)
            movie_id=request.POST["movie_id"]
            user_id=request.user.id
            
            if Watchlist.objects.filter(movie_id=movie_id ,   user_id=user_id):
                messages.error(request,"Already added in a  watchlist")
                return redirect("index")    
                
            else:
                movie_instance=Movie.objects.get(id=movie_id)
                user_instance=User.objects.get(id=user_id)
                addinwatchlist=Watchlist.objects.create(movie=movie_instance,user=user_instance)
                addinwatchlist.save()
                
                print(addinwatchlist.movie.id)
                messages.success(request,"Your movie successfully added in watchlist")
                return redirect("index") 
        else:
                messages.error(request,"Please login and then try")
                return redirect("login")
        
def addInWatchlist_2(request):
    # print(w_id)
    if request.user.is_authenticated:
        
        if request.method=="POST":
            # request.POST
            print(request.POST)
            movie_id=request.POST["movie_id"]
            user_id=request.user.id
            
            if Watchlist.objects.filter(movie_id=movie_id ,   user_id=user_id):
                messages.error(request,"Already added in a  watchlist")
                return redirect("movie",movie_id)    
                
            else:
                movie_instance=Movie.objects.get(id=movie_id)
                user_instance=User.objects.get(id=user_id)
                addinwatchlist=Watchlist.objects.create(movie=movie_instance,user=user_instance)
                addinwatchlist.save()
                
                print(addinwatchlist.movie.id)
                messages.success(request,"Your movie successfully added in watchlist")
                return redirect("movie",movie_id) 
        else:
                messages.error(request,"Please login and then try")
                return redirect("login")
        
def getWatchlist():
    return 