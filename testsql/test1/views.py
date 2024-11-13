

from django.shortcuts import render

from .models import Product

def show(r):
    data = Product.objects.all()
    my_dict = {'data':data}
    return render(r,'test1/product.html',context=my_dict)