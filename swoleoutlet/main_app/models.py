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
<<<<<<< HEAD
  # image = models.ImageField(upload_to="main_app/static/css/images", null=True, blank=True)
  orders = models.ManyToManyField(Order, null = True, blank=True)


=======
  # image = models.ImageField(upload_to="main_app/static/css/images")
  image = models.ImageField(upload_to="main_app/static/css/images", null=True, blank=True)
  orders = models.ManyToManyField(Order, null = True, blank=True)
>>>>>>> 498b4e5f9c821e62c97a888f264a7ab24e683a44

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'product_id':self.id})




    
      

