from django.shortcuts import render

from .forms import feedback_form


# Create your views here.

def show(r):
    form = feedback_form()
    my_dict = {'form': form}
    return render(r, 'formapp/feedback.html', context=my_dict)
