from email.mime import image
from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)
  product_type = models.CharField(max_length=100)
  price = models.IntegerField()
  quantity_available = models.IntegerField()
  product_description = models.TextField(max_length=250)
  #image = models.ImageField(upload_to="images/")

  def __str__(self):
        return self.name

