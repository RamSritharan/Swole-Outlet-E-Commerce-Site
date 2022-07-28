from itertools import product
import stripe
from django.conf import settings
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Product, Order
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin



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


class OrderList(LoginRequiredMixin, ListView):
  model = Order

class OrderDetail(LoginRequiredMixin, DetailView):
  model = Order


class OrderCreate(LoginRequiredMixin, CreateView):
  model = Order
  fields = '__all__'

class OrderUpdate(LoginRequiredMixin, UpdateView):
  model = Order
  fields = ['name', 'color']

class OrderDelete(LoginRequiredMixin, DeleteView):
  model = Order
  success_url = '/orders/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('products')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def cart_index(request):
  total=0
  for item in cart.items.all():
    total += item.price
    cart_total = total
    total_items = len(cart.items.all())
    
  return render(request, 'products/cart.html', {'cart':cart, 'cart_total':cart_total, 'total_items':total_items})


class CreateCheckoutSeshView(View):
  def post(self, request, *args, **kwargs):
    YOUR_DOMAIN = "http://localhost:8000/"
    checkout_session = stripe.checkout.Session.create ( #storing stripe api in variable checkout session
      payment_method_types = ["card"],
      line_items=[
          {
            'price': '{{Product.price}}','quantity': 1, #price related to product id 
          },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success.html',
        cancel_url=YOUR_DOMAIN + '/cart',
    )
    return JsonResponse({ #takes a dict
      "id": checkout_session.id #use id on front end for unique stripe checkout session
    })   

