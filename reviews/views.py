import imp
from django.shortcuts import redirect, render
from django.contrib import messages
from pages.models import Movie
from django.core.mail import send_mail
from reviews.models import Review
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User 
# Create your views here.


def index(request,review_id):
    
    print(review_id)
    return render(request,"review/index.html")


def deleteReview(request):
    
    if request.method=="GET":
        movie_id=request.GET['movie_id']
        review_id=request.GET['review_id']
        
        print(request.GET,"get data")
        
        Review.objects.filter(id=review_id).delete()
      
        messages.success(request,"Your review is successfully deleted")
                
        return redirect("movie",movie_id)
        
        
        # return 
    




def reviewForm(request):
    
    if request.method=="POST":
        message=request.POST["message"]
        movie_id=request.POST["m_id"]
        
        rate=request.POST.get("rate")
        rating=0
        if rate:
            rating=6-int(rate) 
        else:
            rating=0
        print(rate,"rate")
        print(request.POST)
        # print(request.user.id,"user-id")d
        
        
        review=Review.objects.create(message=message,rating=rating,movie_id=movie_id,user_id=request.user.id)
        review.save()
        messages.success(request,"Your review is successfully added")
        send_mail(
            "Movie Review",
            "Your review is successfully submitted",
            "manasrathore2342@gmail.com",
            ["aanshrathore123@gmail.com"],fail_silently=False
        )
        return redirect("movie",movie_id)

# def loginFunc(request):
#     if request.method=="POST":
#         username=request.POST.get("username")
#         password=request.POST.get("password")
        
#         # user=User.objects.get(email=username)
#         print(request.POST)
        
#         user=authenticate(username=username,password=password)
        
        
#         print(user, "userAuthenticate")
        
#         #? USER AUTHENTICATED OR NOT
#         if user is not None:
            
#             login(request,user)
            
#             messages.success(request,"you are logged in now") 
#             return redirect("index")
#             # if userAuthentication!=None:
                
           
             
#             #  return redirect("index")
         
#             # else:
                
#             # # ? USER HAVE INVALID CRED
#             #  messages.error(request,"INVALID CREDENTIALS")
                
#             #  return redirect("login2")
#         else:
            
#             #? USER EMAIL DOESN'T EXIST
#             messages.error(request,"invalid credentials")
#             return redirect("login2")
        
    
#     return render(request,"accounts/login2.html")
# def reg(request):
    
    
    # if request.method =="POST":
        
        
    #     password=request.POST.get("password")
    #     cpassword=request.POST.get("cpassword")
    #     last_name=request.POST.get("lastname")
    #     email=request.POST.get("email")
    #     username=request.POST.get("username")
    #     first_name=request.POST.get("firstname")
        
    #     print(request.POST)
        
    #     if password ==cpassword:
        
    #       userExist=User.objects.filter(username=username)
         
    #       if userExist !=None :
             
    #          user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=cpassword,username=username)
             
             
    #          user.save()
    #          login(request,user)
    #          messages.success(request,"You are logged in now")
    #          return redirect("index")
             
    #       else:
    #          messages.error(request,"invalid credential")
             
    #          return redirect("reg2")
        
    #     else:
    #         messages.error(request,"password does not match")
    #         return redirect("reg2")
    
    
    # return render(request,"accounts/register2.html")
    