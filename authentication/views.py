from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from Rider.models import Riders 
# Create your views here.

def home(request):
    all_members = Riders.objects.all
    return render(request,"authentication/index.html",{'all':all_members})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']    
        lname = request.POST['lname']    
        email = request.POST['email']
        password = request.POST['password']    
        
        myuser = User.objects.create_user(username, email, password)
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')
        myuser.first_name = fname
        myuser.last_name = lname

        messages.success(request,"Your account has been successfully created")
        return redirect('/login')
    return render(request,"authentication/signup.html")

def login_user(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            fname= user.first_name
            return render(request,"authentication/drive_or_ride.html", {'fname':fname})
            
        else:
            messages.error(request,'Wrong username or password, Check again')
            return redirect('/login')
        
    return render(request,"authentication/login.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('/index')

def driveorride(request):
    return render(request,"authentication/drive_or_ride.html")



def Driver(request):
    return render(request,"authentication/Driver.html")


def Rider(request):
    return render(request,"authentication/Rider.html")