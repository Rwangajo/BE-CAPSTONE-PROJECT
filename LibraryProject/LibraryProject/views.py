from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

@login_required
def borrow_page(request):
    return render(request, 'borrow.html')

def logout_user(request):
    logout(request)
    return redirect('login_page')
