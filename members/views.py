from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Importing the Registered UserForm
from members.forms import RegisterUserForm


def login_user(request):
    """
        This view is used to log users in
    """
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,("User Credential Wrong"))
            return redirect('login')
    else:
        
        return render(request,'accounts/login.html' )

def logout_user(request):
    """
        This view is used to log users out and redirect them to home page
    """
    logout(request)
    messages.success(request,("You have been logged out"))
    return redirect('home')


def register_user(request):
    """
        This view is used to register a new user 

        user information is then stored in the database 

        Users are redirected to homepage
    """
    if request.method =="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("Registration Successfull"))
            return redirect('home')
    else:
        form = RegisterUserForm()

 
    return render(request, 'accounts/register_user.html',{
        'form':form
    })
