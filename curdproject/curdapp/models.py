from django.db import models

# Create your models here.
class student_data(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    admissions_date = models.DateField()
    create_record = models.DateTimeField(auto_now_add=True)