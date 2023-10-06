from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.clients, name='clients'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
]
