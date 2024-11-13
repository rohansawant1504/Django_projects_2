from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def dev_env(r):
    return HttpResponse("<h1> this is dev env </h1>")
