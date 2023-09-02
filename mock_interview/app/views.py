from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request, 'app/index.html')

def upload_resume(request):
    return render(request, 'app/upload.html')

def signup(request):
    return render(request, 'app/signup.html')

def login(request):
    return render(request, 'app/login.html')