from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True, default="TEMP-SKU")
    name = models.CharField(max_length=100)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )

    size = models.CharField(max_length=20, default="")
    color = models.CharField(max_length=50, default="")

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.IntegerField()

    barcode = models.CharField(
    max_length=100,
    unique=True,
    default="TEMP-BARCODE"
)

    created_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name