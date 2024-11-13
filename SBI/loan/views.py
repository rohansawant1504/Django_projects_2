from django.shortcuts import render

# Create your views here.

def SBI_home_loan(r):
    my_dict = {'name':'Rohan','id':154}
    return render (r,'loan/home_loan.html',context=my_dict)

def SBI_car_loan(r):
    return render (r,'loan/car_loan.html')