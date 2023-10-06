from django.http import HttpResponse
from django.shortcuts import render
from hw2app.models import Client, Product, Order

# Create your views here.
def clients(request):
    return HttpResponse(Client.objects.all())

def products(request):
    return HttpResponse(Product.objects.all())

def orders(request):
    return HttpResponse(Order.objects.all())