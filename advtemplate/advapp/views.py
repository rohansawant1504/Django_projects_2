from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'advapp/home.html')

def index(request):
    return render(request, 'advapp/index.html')

def about(request):
    return render(request, 'advapp/about.html')

def logout(request):
    return render(request, 'advapp/logout.html')

@login_required
def apply(request):
    return render(request, 'advapp/apply.html')
