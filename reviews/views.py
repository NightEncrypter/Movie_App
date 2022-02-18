from django.shortcuts import redirect, render
from django.contrib import messages

from reviews.models import Review
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User 
# Create your views here.


def index(request,review_id):
    
    print(review_id)
    return render(request,"review/index.html")



def reviewForm(request):
    
    if request.method=="POST":
        message=request.POST["message"]
        movie_id=request.POST["m_id"]
        print(request.POST)
        print(request.user.id,"user-id")
        
        
        review=Review.objects.create(message=message,rating=4,movie_id=movie_id,user_id=request.user.id)
        review.save()
        
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
    