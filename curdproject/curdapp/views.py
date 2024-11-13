from django.shortcuts import render
from .forms import student_forms
from .models import student_data
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.

def index(r):
    data = student_data.objects.all()
    return render(r,"curdapp/index.html",{'data':data})

def create(r):
    form = student_forms()
    if r.method == "POST":
        form = student_forms(r.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/index')
    return render(r,'curdapp/create.html',{'form':form})

def delete(r,id):
    data = student_data.objects.get(roll=id)
    data.delete()
    return HttpResponseRedirect('/index')

def update(r,id):
    data = student_data.objects.get(roll=id)
    if data:
        if r.method == "POST":
            if r.POST['roll'] == str(data.roll):
                form = student_forms(r.POST,instance=data)
                if form.is_valid():
                    form.save(commit=True)
                    return HttpResponseRedirect('/index')
            else:
                return HttpResponse("Record Not Found for given number")

    return render(r,'curdapp/update.html',{'data':data})