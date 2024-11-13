from django.shortcuts import render
from django.http  import HttpResponse
import datetime
# Create your views here.
def showdate(r):
     c_date = datetime.datetime.now()
     return HttpResponse("<h1> current date is:"+str(c_date)+"</h1>")