from django.db import models
import random
from django.utils import timezone
from products.models import Product
from django.utils.translation import gettext as _
# Create your models here.
def generaste_code(length=8):
    numbers = "0123456789"
    return "".join(random.choice(numbers) for _ in range(length))

STATUS_CHOICES = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)

class Order(models.Model):
    code = models.CharField(max_length=8, default=generaste_code)
    order_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.code)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order_detail"),related_name="order_detail",on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"),related_name="order_product",on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return str(self.order)