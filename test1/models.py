from itertools import product
from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.IntegerField()

class cart(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100, default=None)
    quantity=models.IntegerField()
    price=models.IntegerField()
    user=models.CharField(max_length=100)


class Feedback(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    feedback=models.TextField(max_length=300)
