from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, UserLoginForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User registered:", user)
            user_profile = UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('welcome', username=user.username)
        else:
            print("Form errors:", form.errors)
    else:
        form = UserRegistrationForm()

    return render(request, 'register/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome', username=user.username)  # Замените 'home' на URL вашей главной страницы
        else:
            print("Form errors:", form.errors)
    else:
        form = UserLoginForm()

    return render(request, 'login/login.html', {'form': form})


def welcome(request, username=None):
    return render(request, 'welcome/welcome.html', {'username': username})
