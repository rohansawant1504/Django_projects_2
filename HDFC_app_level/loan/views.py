from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def personal_loan(r):
    return HttpResponse("<h1> this is personal loan department thanks for visit </h1>")
def home_loan(r):
    return HttpResponse("<h1> this is Home loan department thanks for visit </h1>")
def car_loan(r):
    return HttpResponse("<h1> this is Car loan department thanks for visit </h1>")
