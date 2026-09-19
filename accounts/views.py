from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomLoginForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('student-list')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='accounts.backends.EmailOrUsernameModelBackend')
            return redirect('student-list')
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/signup.html", {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('student-list')

    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student-list')
    else:
        form = CustomLoginForm()

    return render(request, "accounts/login.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
