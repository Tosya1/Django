from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from hw2app.models import Client, Product, Order

# Create your views here.


def index(request):
    return render(request, "hw2app/base.html", {"title": "Main"})


def clients(request):
    return render(
        request,
        "hw2app/clients.html",
        {"title": "Clients", "clients": Client.objects.all()},
    )


def client_by_id(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(
        request, "hw2app/client.html", {"title": f"{client.name}", "client": client}
    )


def products(request):
    return render(
        request,
        "hw2app/products.html",
        {"title": "Products", "products": Product.objects.all()},
    )


def product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(
        request, "hw2app/product.html", {"title": f"{product.name}", "product": product}
    )


def orders(request):
    return HttpResponse(Order.objects.all())


def orders_by_client_id(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client).order_by("date_ordered")
    return render(
        request,
        "hw2app/orders_by_client_id.html",
        {"title": f"Orders by {client.name}", "orders": orders},
    )


def ordered_products_for_period(request, client_id, period):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(
        client=client, date_ordered__gt=datetime.now() - timedelta(days=period)
    )
    products = set()
    for order in orders:
        products.update(order.products.all())
    return render(
        request,
        "hw2app/products_for_period.html",
        {
            "title": f"Ordered products by {client.name} ",
            "products": products,
            "period": period,
        },
    )
