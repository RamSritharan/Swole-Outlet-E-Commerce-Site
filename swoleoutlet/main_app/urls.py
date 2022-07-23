from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('products/', views.products_index, name='products'),
#   path('products/<int:product_id>/', views.products_detail, name='detail'),
]
