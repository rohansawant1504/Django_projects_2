from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    price = models.FloatField()
    qty = models.IntegerField()

