from operator import mod
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='static/images/' )
    price = models.IntegerField()
    specification = models.CharField(max_length = 50)

