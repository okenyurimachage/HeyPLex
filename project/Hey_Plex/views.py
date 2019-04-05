from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,'Hey_Plex/home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'You have successfully logged in dear...')
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Wrong Username/Password.Try again')
            return redirect('login')
    else:
     return render(request,'Hey_Plex/login.html', {})

def details(request):
    return render(request,'Hey_Plex/details.html', {})

def signup_user(request):
    return render(request,'Hey_Plex/signup.html', {})

def logout_user(request):
    logout(request)
    # messages.success(request, 'You have been successfully logged out')
    return redirect('login')
    # Redirect to a success page.

