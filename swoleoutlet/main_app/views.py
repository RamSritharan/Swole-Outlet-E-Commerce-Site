from itertools import product
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, JsonResponse
from .models import Product, Order
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.urls import reverse
from django.conf import settings  
import os




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
  return render(request, "products/cart.html", {})


def checkout_index(request):
  return render(request, "products/checkout_list.html", {})


def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', { 'products': products })


#@csrf_exempt
# @urls.route('/create-checkout-session', methods=['POST'])
# def checkout(request):
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=[{
#             'price': 'price_1LQengKrU0xm2AHUxOwXItn8',
#             'quantity': 1,
#         }],
#         mode='payment',
#         success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
#         cancel_url=request.build_absolute_uri(reverse('about')),
#     )

#     return JsonResponse({
#         'session_id' : session.id,
#         'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
#     })


def thanks(request):
    return render(request, 'thanks.html')