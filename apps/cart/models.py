from django.db import models
from apps.movie.models import Movie
from apps.account.models import CustomerUser
import datetime


class CartMovie(models.Model):
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def get_movie_price(self):
        return self.movie.price


class Cart(models.Model):
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    movies = models.ManyToManyField(CartMovie)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart Id: %s by user: %s" % (self.id, self.user_id)

    def get_total(self):
        total = 0
        for movie in self.movies.all():
            total += movie.get_movie_price()
        return total
