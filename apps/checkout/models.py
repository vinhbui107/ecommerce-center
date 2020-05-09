from django.db import models
from apps.account.models import CustomerUser
from apps.cart.models import Cart
from django.utils import timezone


class Order(models.Model):
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    fullname = models.CharField(default="", max_length=100, null=True)
    shipping_address = models.CharField(default="", max_length=255)
    phone_number = models.IntegerField(null=True)
    order_description = models.CharField(default="", max_length=255)
    order_total = models.DecimalField(max_digits=9, decimal_places=2)
    is_complete = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now, editable=False)
    update_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.create = timezone.now()
        self.update_date = timezone.now()
        return super(Order, self).save(*args, **kwargs)
