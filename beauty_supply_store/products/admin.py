from django.contrib import admin
from .models import Products, Producers, Categories, Orders, OrderProducts

admin.site.register(Products)
admin.site.register(Producers)
admin.site.register(Categories)
admin.site.register(Orders)
admin.site.register(OrderProducts)
