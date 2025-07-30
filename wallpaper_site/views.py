from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request,'login_app/index.html',{})

def login(request):
    return render(request, 'login_app/login.html', {})

def signup(request):
    return render(request, 'login_app/signup.html', {})

def desktop(request):
    return render(request,'login_app/desktop.html')

def mobile(request):
    return render(request,'login_app/mobile.html')

def index_2(request):
    return render(request, 'login_app/index_2.html')