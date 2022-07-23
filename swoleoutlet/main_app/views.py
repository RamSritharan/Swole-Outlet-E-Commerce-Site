from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', { 'products': products })


def products_detail(request, product_id):
    cat = Product.objects.get(id=product_id)
    return render(request, 'product/detail.html', { 'cat': cat })