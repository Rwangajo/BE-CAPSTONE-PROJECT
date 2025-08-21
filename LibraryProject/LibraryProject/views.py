from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    Home page for the Library Project
    """
    return render(request, 'home.html', {
        'title': 'Library Management System',
        'description': 'Welcome to the Library Management System'
    })

def home_simple(request):
    """
    Simple home page that returns plain text
    """
    return HttpResponse("Welcome to the Library Management System!")