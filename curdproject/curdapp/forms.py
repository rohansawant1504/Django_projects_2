from django import forms
from .models import student_data

class student_forms(forms.ModelForm):
    class Meta:
        model = student_data
        fields = '__all__'
