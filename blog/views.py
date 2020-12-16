from django.shortcuts import render
from django.utils import timezone
from .models import Post

def home(request):
    return render(request, 'blog/home.html', {})

def intro(request):
    return render(request, 'blog/intro.html', {})

def emojomo(request):
    return render(request, 'blog/emojomo.html', {})

def team(request):
    return render(request, 'blog/team.html', {})
