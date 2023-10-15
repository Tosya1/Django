
from datetime import datetime, timedelta
from random import choices, randint
from django.core.management.base import BaseCommand
from hw2app.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake authors and articles."

    def add_arguments(self, parser):
        parser.add_argument("client_id", type=int, help="Client_id")
        parser.add_argument("product_count", type=int, help="Product_count")

    def handle(self, *args, **kwargs):
        client_id = kwargs.get("client_id")
        product_count = kwargs.get("product_count")
        client = Client.objects.filter(pk=client_id).first()
        order = Order(client=client)
        order.save()
        order.products.set(
            choices(Product.objects.all(), k=randint(1, product_count))
        )
        order.date_ordered = datetime.now() - timedelta(days=7)
        order.set_total_price()
        order.save()