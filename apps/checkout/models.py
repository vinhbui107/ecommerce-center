from django.db import models
from apps.account.models import CustomerUser
from apps.cart.models import Cart


class Order(models.Model):
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    order_description = models.CharField(default="", max_length=255)
    order_total = models.DecimalField(max_digits=9, decimal_places=2)
    is_complete = models.BooleanField(default=False)
