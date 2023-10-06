from random import choices, randint
from django.core.management.base import BaseCommand
from hw2app.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake authors and articles."

    def add_arguments(self, parser):
        parser.add_argument("client_count", type=int, help="Client count")
        parser.add_argument("product_count", type=int, help="Product_count")

    def handle(self, *args, **kwargs):
        client_count = kwargs.get("client_count")
        product_count = kwargs.get("product_count")

        for i in range(1, product_count + 1):
            product = Product(name=f"Product{i}", price=i * 1.11, count=i * 10)
            product.save()
        for i in range(1, client_count + 1):
            client = Client(
                name=f"Name{i}",
                email=f"mail{i}@mail.ru",
                tel_number="111111111111",
                address=f"adress{i}",
            )
            client.save()
            order = Order(client=client)
            order.save()
            order.products.set(
                choices(Product.objects.all(), k=randint(1, product_count))
            )
            order.set_total_price()
            order.save()
