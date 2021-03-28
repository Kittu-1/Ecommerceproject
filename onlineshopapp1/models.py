from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ProductModel(models.Model):
    Title= models.CharField(max_length=50,default=True)
    Description= models.TextField()
    Image_link= models.URLField()
    Price= models.FloatField(default=True)
    created_on = models.DateField(auto_now_add=True,editable=False)
    updated_on = models.DateField(auto_now=True,editable=False)

    def __str__(self):
        return self.Title


STATUS_CHOICES = (
    ('new', 'new'),
    ('paid', 'paid')
)

MODE_OF_PAYMENT = (
    ('cash', 'cash'),
)


class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Total = models.IntegerField(default=0)
    Order_placed_on = models.DateField(auto_now_add=True)
    Order_updated_on = models.DateField(auto_now=True)
    Status= models.CharField(choices=STATUS_CHOICES, max_length=5)
    Mode_of_payment = models.CharField(choices=MODE_OF_PAYMENT, max_length=25)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.Title


class OrderItemsModel(models.Model):
    order_Id = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product_Id = models.ForeignKey(ProductModel, on_delete=models.CASCADE,default=True)
    Quantity= models.IntegerField(default=1)
    Price = models.FloatField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_Id.Title