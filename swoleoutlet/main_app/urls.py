from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('products/', views.products_index, name='products'),
  path('products/<int:product_id>/', views.products_detail, name='detail'),
  # associate a order with a product (M:M)
  path('products/<int:product_id>/assoc_order/<int:order_id>/', views.assoc_order, name='assoc_order'),
  # unassociate a order and product
  path('products/<int:product_id>/unassoc_toy/<int:order_id>/', views.unassoc_order, name='unassoc_order'),
  path('orders/', views.OrderList.as_view(), name='Orders_index'),
  path('orders/<int:pk>/', views.OrderDetail.as_view(), name='Orders_detail'),
  path('orders/create/', views.OrderCreate.as_view(), name='Orders_create'),
  path('orders/<int:pk>/update/', views.OrderUpdate.as_view(), name='Orders_update'),
  path('orders/<int:pk>/delete/', views.OrderDelete.as_view(), name='Orders_delete'),

]
