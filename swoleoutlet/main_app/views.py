from itertools import product
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Product, Order


# Define the home view
def home(request):
  return redirect('about') 

def about(request):
  return render(request, 'about.html')

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', { 'products': products })


def products_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product/detail.html', { 'product': product  })

def assoc_order(request, product_id, order_id):
  Product.objects.get(id=product_id).orders.add(order_id)
  return redirect('detail', product_id=product_id)

def unassoc_order(request, product_id, order_id):
  Product.objects.get(id=product_id).orders.remove(order_id)
  return redirect('detail', product_id=product_id)



class OrderList(ListView):
  model = Order

class OrderDetail(DetailView):
  model = Order

class OrderCreate(CreateView):
  model = Order
  fields = '__all__'

class OrderUpdate(UpdateView):
  model = Order
  fields = ['name', 'color']

class OrderDelete(DeleteView):
  model = Order
  success_url = '/toys/'