from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def loginUser(request):

    if request.user.is_authenticated:
        return redirect('posts')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts')
        else:
            messages.error(request, "Username OR Password is incorrect")

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('edit-account')
        
        else:
            messages.error(request, 'An error occurred during registration')

    context = {
            'page': page, 
            'form': form
        }
    return render(request, 'users/login_register.html', context)

@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile 

    context = {
        "profile": profile
    }
    return render(request, 'users/account.html', context)

@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {
        "form": form
    }
    return render(request, 'users/profile_form.html', context)