from django.shortcuts import render
from .forms import feedback_form


# Create your views here.
def show(r):
    form = feedback_form
    my_dict1 = {'form':form}
    if r.method == 'POST':
        form = feedback_form(r.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    return render(r,'modelapp/feedback.html',context=my_dict1)
