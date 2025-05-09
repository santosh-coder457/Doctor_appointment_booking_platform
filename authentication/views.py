from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

def loginpage(request):

    context = {
        "error":""
    }

    if request.method == "POST":

        print(request.POST)

        user =authenticate(username = request.POST['username'],password=request.POST['password'])

        print(user)

        if user is not None:

            login(request,user)

            return redirect('/MedguardHome/dashpage/')
        else:

            context = {
                "error" : "Invalid User or Password"
            }

    return render(request,'login-signup.html',context)

def logoutuser(request):

    logout(request)

    return redirect('/')


def signup(request):

    context={
        "error" : ""
    }

    if request.method == "POST":

        user_check = User.objects.filter(username= request.POST['username'])

        if len(user_check) >0:
           
           context= {
               "error" : "* username already exists"
           }

           return render(request,'signup.html',context)

        else:

            new_user = User(username= request.POST['username'],first_name=request.POST['firstname'],
                            last_name=request.POST['lastname'],email=request.POST['email'])
            
            new_user.set_password(request.POST['password'])

            new_user.save()

            return redirect('/')

        

    return render(request,'signup.html',context)