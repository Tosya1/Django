from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('clients/<int:client_id>/', views.client_by_id, name='client_by_id'),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>', views.product_by_id, name='product_by_id'),
    path('orders/', views.orders, name='orders'),
    path('clients/<int:client_id>/orders/', views.orders_by_client_id, name='orders_by_client_id'),
    path('clients/<int:client_id>/products/week/', views.ordered_products_for_period, {'period': 7}, name='ordered_products_per_week'),
    path('clients/<int:client_id>/products/month/', views.ordered_products_for_period, {'period': 30}, name='ordered_products_per_month'),
    path('clients/<int:client_id>/products/year/', views.ordered_products_for_period, {'period': 365}, name='ordered_products_per_year'),
]
