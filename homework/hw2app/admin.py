from django.contrib import admin
from django.utils.html import format_html
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "tel_number", "address", "regisrtation_date"]
    ordering = ["name"]
    list_filter = ["regisrtation_date"]
    list_per_page = 10
    search_fields = ["name"]
    search_help_text = "Поиск по полю Имя клиента"
    fields = ["name", "email", "tel_number", "address"]


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "client",
        "ordered_products",
        "date_ordered",
        "total_price",
    ]
    ordering = ["date_ordered", "client__name"]
    list_filter = ["date_ordered"]
    list_per_page = 10
    search_fields = ["client__name"]
    search_help_text = "Поиск по полю Клиент"
    fields = ["client", "products"]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "price",
        "count",
        "created_at",
        "product_image",
    ]
    ordering = ["name"]
    list_filter = ["price", "count"]
    list_per_page = 10
    search_fields = ["description", "name"]
    search_help_text = "Поиск по полю Описание продукта"
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["name"],
            },
        ),
        (
            "Подробности",
            {
                "classes": ["collapse"],
                "description": "Категория товара и его подробное описание",
                "fields": ["description", "image"],
            },
        ),
        ("Бухгалтерия", {"fields": ["price", "count"]}),
    ]

    def product_image(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width ="30", height="30"/>')


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
