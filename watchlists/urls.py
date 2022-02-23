from django.urls import  path

from . import views

urlpatterns=[
    
    path("",views.watchlistData,name="watchlist"),
    path("addinwatchlist",views.addInWatchlist,name="addwatchlist"),
    path("addinwatchlist_2",views.addInWatchlist_2,name="addwatchlist_2"),
]