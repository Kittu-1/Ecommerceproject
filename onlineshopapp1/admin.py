from django.contrib import admin

# Register your models here.
from onlineshopapp1.models import ProductModel,OrderModel, OrderItemsModel

admin.site.register(ProductModel)
admin.site.register(OrderModel)
admin.site.register(OrderItemsModel)