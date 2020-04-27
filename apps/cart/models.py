from django.db import models
from apps.movie.models import Movie
from apps.account.models import CustomerUser
import datetime
from django.utils import timezone


class CartMovie(models.Model):
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def get_movie_price(self):
        return self.movie.price


class Cart(models.Model):
    user_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    movies = models.ManyToManyField(CartMovie)
    create_date = models.DateTimeField(default=timezone.now, editable=False)
    update_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def get_total(self):
        total = 0
        for movie in self.movies.all():
            total += movie.get_movie_price()
        return total

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.update_date = timezone.now()
        return super(Cart, self).save(*args, **kwargs)
