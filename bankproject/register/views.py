from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User exists")
                print("user exists")
                return redirect('register:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exists")
                print("email exists")
                return redirect('register:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save()
                messages.success(request,"Created")
                print("user created")
                return redirect('register:login')
        else:
            messages.info(request, "password Error")
            print("check password")
            return redirect('register:register')
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invlid username or password")
            return redirect('register:login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)

    return redirect('/')