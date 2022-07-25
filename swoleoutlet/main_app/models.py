#from email.mime import image
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Order(models.Model):
  date = models.DateField('order date')
  products = models.CharField(max_length=100)
  quantity_purchased = models.IntegerField()
  total = models.IntegerField() 
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
    return reverse('Orders_detail', kwargs={'pk': self.id})


class Product(models.Model):
  name = models.CharField(max_length=100)
  product_type = models.CharField(max_length=100)
  price = models.IntegerField()
  quantity_available = models.IntegerField()
  product_description = models.TextField(max_length=250)
  #image = models.ImageField(upload_to="images/")
  orders = models.ManyToManyField(Order)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'product_id':self.id})


# class customer(models.Model)
#   name = models.CharField(max_length=100)
#   customer_address = models.CharField(max_length=100)
#   customer_city = models.CharField(max_length=100)
#   #user = models.ForeignKey(User, on_delete=models.CASCADE)
#   orders = models.ForeignKey(Order, on_delete=models.CASCADE)

#   def __str__(self):
#       return self.name


    
      

