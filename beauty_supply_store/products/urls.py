from django.urls import path
from products.views import *

urlpatterns = [
    path ('category/<id>/', category, name='category'),
    path('product/<id>/', product_id, name='product_id'),
]