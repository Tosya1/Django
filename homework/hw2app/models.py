from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tel_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    regisrtation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.email}, tel: {self.tel_number}, address: {self.address}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Нет информации")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'client: {self.client.name}, products: {", ".join([f"{product.name}, price: {product.price}" for product in self.products.all()])}, total_price: {self.total_price}'

    def set_total_price(self):
        products = self.products.all()
        self.total_price = sum(product.price for product in products)
