# This example sets up an endpoint using the Flask framework.
# Watch this video to get started: https://youtu.be/7Ul1vfmsDck.
from django.shortcuts import render
from django.conf import settings

import os
import stripe

from flask import Flask, redirect

app = Flask(__name__)

stripe.api_key = settings.STRIPE_PRIVATE_KEY

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
  session = stripe.checkout.Session.create(
    line_items=[{
     'price': 'price_1LQengKrU0xm2AHUxOwXItn8',
     'quantity': 1,
    }],
    mode='payment',
    success_url='http://localhost:8000/success.html',
    cancel_url='https://example.com/cancel',
  )

  context = {
    'session_id' : session.id,
    'stripe_public_key' :settings.STRIPE_PUBLIC_KEY,
  }

  return redirect(session.url, code=303)

if __name__== '__main__':
    app.run(port=4242)