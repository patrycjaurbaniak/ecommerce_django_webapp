from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager


class Producers(models.Model):
    def __str__(self):
        return self.brand_name

    brand_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"


class Categories(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Products(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    producer = models.ForeignKey(Producers, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Categories, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.0)])
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "products"


class Orders(models.Model):
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderProducts(models.Model):
    ordered_products = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "OrderProduct"
        verbose_name_plural = "OrderProducts"
