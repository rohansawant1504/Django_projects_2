from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def test_env(r):
    return HttpResponse("<h1> This is test env </h1>")