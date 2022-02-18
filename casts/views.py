from django.shortcuts import render

# Create your views here.


def index(request,cast_id):
    
    print(cast_id)
    return render(request,"cast/index.html")