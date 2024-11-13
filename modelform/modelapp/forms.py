from django.db import models
from django import forms
from .models import modelapp_model_form_user

class feedback_form(forms.ModelForm):
    class Meta:
        model = modelapp_model_form_user
        fields = '__all__'

