from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField()
    tel_number = models.CharField(max_length=30, verbose_name="Телефон")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    regisrtation_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации"
    )

    def __str__(self):
        return f"{self.name}, email: {self.email}"

    class Meta:
        verbose_name = "Клиента"
        verbose_name_plural = "Клиенты"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(
        default="Нет информации", verbose_name="Краткое описание"
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    count = models.IntegerField(verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    image = models.ImageField(null=True, blank=True, default=None, verbose_name="Фото")

    def __str__(self):
        return f"{self.name}, price: {self.price}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    products = models.ManyToManyField(Product, verbose_name="Товары")
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    total_price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, verbose_name="Общая стоимость"
    )

    def __str__(self):
        return f"Заказ №{self.client.id}, клиент: {self.client.name}, стоимость заказа: {self.total_price}"

    def set_total_price(self):
        products = self.products.all()
        self.total_price = sum(product.price for product in products)

    def ordered_products(self):
        return ", ".join([product.name for product in self.products.all()])

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
