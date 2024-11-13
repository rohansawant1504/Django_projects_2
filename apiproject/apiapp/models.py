from django.db import models

# Create your models here.
class employee_data(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=30)
    emp_sal = models.IntegerField()
    emp_city = models.CharField(max_length=30)
