from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# @login_required(login_url="/login/")
def index(request):
    return render(request , 'index.html')

@login_required(login_url="/login/")
def home(request):
    return render(request , 'index.html')

def log_in(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username.")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request, "Invalid Credentials.")
            return redirect('/login/') 
        else:
            login(request, user)
            return redirect('/home/') 


    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('/login/')

def signup(request):

    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "User name already taken. Try another username.")
            return redirect('/login/')

        user = User.objects.create(
            username = username, 
            first_name = first_name,
            last_name = last_name,
            email = email
        ) 

        user.set_password(password)
        user.save()
        messages.info(request, "User created succesfully.")
        return redirect('/login/')  

    return render(request, 'signup2.html')







