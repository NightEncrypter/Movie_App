from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.


def login(request):
    search=False
    # ham=FalseS
    register=True
    login=False
    context={"search":search,"register":register,"login":login}
    if request.method=="POST":
        
        
        
        email=request.POST.get("email").lower()
        password=request.POST.get("password")
        
        print(request.POST)
        
        # print(User.objects.get(username=email),"get")   
        
        #? CHECK EMAIL EXIST OR NOT  
        if User.objects.filter(username=email).exists(): 
            
            #? CHECK USER AND PASSWORD IN DATABASE
            user=auth.authenticate(request,username=email,password=password)
            
            
            print(user)
            
            if user != None :
                
                #? then Login to user
                auth.login(request,user)
                messages.success(request,"you are now logged in")
                return redirect("index")
            
            else:
                messages.error(request,"Error Invalid Credentials")
                return redirect("login")
        else:
            messages.error(request,"Error email id does not exist")
            return redirect("login")
            
            
            
    
        
        
    else:   
     return render(request,"accounts/login.html",context)

def register(request):
    search=False
    # ham=False
    login=True
    register=False
    context={"search":search,"login":login,"register":register}
    
    
    if request.method=="POST":
        
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]
        first_name=request.POST["firstname"].lower()
        last_name=request.POST["lastname"].lower()
        email=request.POST["email"].lower()
        
        # ? CHECK BOTH PASSWORD FIELDS
        if password == cpassword:
            
            useremail=User.objects.filter(username=email)
            
            print(User.objects.filter(username=email))
            #? Check User exist or nnot 
            if useremail:
                
                
                messages.error(request,"Error user already exist") 
                return redirect("register")
                
            else:
                
                #? LOOKS GOOD
                user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=cpassword,username=email)
                # user.save()  
                
                
                
                #? Authenticate after save the data
                auth.login(request,user)
                
                messages.success(request,"You are logged in now") 
                return redirect("index")
        else:
            messages.error(request,"Error password does not match")
            return redirect("register")
        
        # messages.error(request,"Testing purpose","pta nh kyu")
        # return redirect("register")
    else:
     return render(request,"accounts/register.html",context)
 
 
 
 
def logout(request):
    
    if request.method=="POST":
     auth.logout(request)
     messages.success(request,"You are logout successfully")
     return redirect("login")
        
    # return redirect("login")