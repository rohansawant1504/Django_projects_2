from django.shortcuts import render

# Create your views here.
def index(r):
    return render(r,'tempapp/index.html')

def show(r):
    return render(r,'tempapp/show.html')