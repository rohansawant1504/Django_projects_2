from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, authenticate,login
from .forms import signup_form

from django.http import HttpResponseRedirect


# Create your views here.

def home(r):
    return render(r,'loanapp/home.html')
def about(r):
    return render(r,'loanapp/about.html')
def contact(r):
    return render(r,'loanapp/contact.html')
@login_required
def homeloan(r):
    return render(r,'loanapp/homeloan.html')
def carloan(r):
    return render(r,'loanapp/carloan.html')
def user_logout(r):
    auth_logout(r)
    return render(r,'loanapp/user_logout.html')

# def signup(r):
#     form = signup_form()
#     if r.method == "POST":
#         form = signup_form(r.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return HttpResponseRedirect('/accounts/login')
#
#     return render(r,'loanapp/signup.html',{'form':form})


def signup(r):
    if r.method == 'POST':
        form = signup_form(r.POST)
        if form.is_valid():
            user = form.save(commit=True)  # Create the user
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')  # Redirect to the login page
    else:
        form = signup_form()
    return render(r, 'loanapp/signup.html', {'form': form})

# def signup(r):
#     form = signup_form()
#     if r.method == "POST":
#         form = signup_form(r.POST)
#         if form.is_valid():
#             user = form.save(commit=True)  # Saves the user
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')  # Use password field name from your form
#             # Authenticate and log the user in immediately
#             user = authenticate(r, username=username, password=password)
#             if user is not None:
#                 login(r, User)
#                 return HttpResponseRedirect('/accounts/login')  # Redirect to the login page
#
#     return render(r, 'loanapp/signup.html', {'form': form})