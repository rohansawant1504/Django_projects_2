from django import forms

class feedback_form(forms.Form):
    CHOICES = [('1', 'male'), ('2', 'female')]

    name = forms.CharField(max_length=30)
    city = forms.CharField(max_length=20)
    mobile = forms.IntegerField(max_value=10)
    email = forms.EmailField()
    date = forms.DateField()
    # gender = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)