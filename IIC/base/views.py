from django.shortcuts import render
from .models import posts

# Create your views here.

def home(req):
    post = posts.objects.all()
    context = {"posts" : post}
    return render(req,"home.html" , context)

def loginFac(req):
    return render(req,"login.html")