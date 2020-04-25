from django.db import models
from apps.movie.models import Movie
from apps.account.models import CustomerUser


class OrderMovie(models.Model):
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Movie, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_amount_saved(self):
        return self.get_total_item_price()


class Cart(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderMovie)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_amount_saved()
        return total
