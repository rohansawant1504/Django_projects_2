from django.contrib import admin
from .models import student_data


class student_admin(admin.ModelAdmin):
    list_display = ['roll','name','email','admissions_date','create_record']

admin.site.register(student_data,student_admin)
# Register your models here.
