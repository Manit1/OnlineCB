from django.shortcuts import render
from django.contrib.auth import authenticate,login ,logout
from django.http import HttpResponseRedirect
# Create your views here.

def login_view(request):
    error=""
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username= username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/')      
        else:
            error="Incorrect username or password"
    context={
            "error":error
    }
    return render(request,'auth1/login.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
