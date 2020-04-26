from django.views.generic import View
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.movie.models import Movie
from apps.cart.models import Cart, CartMovie
from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.utils import timezone


class CartDetailView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            cart = Cart.objects.get(user_id=self.request.user, is_active=True)
            context = {"cart": cart}
            return render(self.request, "cart/cart.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return HttpResponseRedirect("/")


@login_required
def add_to_cart(request, slug):
    # the movie has just been added by user
    movie = get_object_or_404(Movie, slug=slug)
    cart_movie, created = CartMovie.objects.get_or_create(
        movie=movie, user_id=request.user, is_active=True
    )
    cart_of_user = Cart.objects.filter(user_id=request.user, is_active=True)

    # check current cart of user
    if cart_of_user.exists():
        cart = cart_of_user[0]
        # check the movie that has been added to the shopping cart by the user
        if cart.movies.filter(movie__slug=movie.slug).exists():
            messages.info(request, "This movie was in your cart!")
            return redirect("cart:cart")
        else:
            cart_movie.update_date = timezone.now()
            cart.movies.add(cart_movie)
            messages.info(request, "This movie just added to your cart.")
            return redirect("cart:cart")
    else:
        # user current have no cart, we'll create a new cart.
        create_date = datetime.now()
        cart = Cart.objects.create(user_id=request.user, create_date=create_date)
        cart.movies.add(cart_movie)
        messages.info(request, "This movie just added to your cart.")
        return redirect("cart:cart")


@login_required
def remove_from_cart(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    cart_of_usert = Cart.objects.filter(user_id=request.user, is_active=True)

    if cart_of_usert.exists():
        cart = cart_of_usert[0]
        # check if the order item is in the order
        if cart.movies.filter(movie__slug=movie.slug).exists():
            cart_movie = CartMovie.objects.filter(
                movie=movie, user_id=request.user, is_active=True
            )[0]
            cart.movies.remove(cart_movie)
            cart_movie.delete()
            cart_movie.update_date = timezone.now()
            messages.info(request, "This item was removed from your cart.")
            return redirect("cart:cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("movie:movie-list", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("movie:movie-list", slug=slug)
