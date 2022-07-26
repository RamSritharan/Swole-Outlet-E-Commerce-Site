from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('products/', views.products_index, name='products'),
  path('cart/', views.cart_index, name='cart'),
  path('checkout/', views.checkout_index, name='checkout'),
  path('products/<int:product_id>/', views.products_detail, name='detail'),
  path('reviews/', views.product, name='reviews'),
  # associate a order with a product (M:M)
  path('products/<int:product_id>/assoc_order/<int:order_id>/', views.assoc_order, name='assoc_order'),
  # unassociate a order and product
  path('products/<int:product_id>/unassoc_order/<int:order_id>/', views.unassoc_order, name='unassoc_order'),
  path('reviews/', views.OrderList.as_view(), name='Orders_index'),
  path('orders/<int:pk>/', views.OrderDetail.as_view(), name='Orders_detail'),
  path('orders/create/', views.OrderCreate.as_view(), name='Orders_create'),
  path('orders/<int:pk>/update/', views.OrderUpdate.as_view(), name='Orders_update'),
  path('orders/<int:pk>/delete/', views.OrderDelete.as_view(), name='Orders_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('thanks/', views.thanks, name='thanks'),
]
