from django.views.generic import View
from django.shortcuts import redirect, render, get_object_or_404
from apps.movie.models import Movie
from apps.cart.models import Cart, OrderMovie
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class CartDetailView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Cart.objects.get(user_id=self.request.user, ordered=False)
            context = {
                'movie': order
            }
            return render(self.request, "cart/cart.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Movie, slug=slug)
    order_item, created = OrderMovie.objects.get_or_create(
        item=item,
        user_id=request.user,
        ordered=False
    )
    order_qs = Cart.objects.filter(user_id=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was update")
            return redirect("movie:movie-detail", the_slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect("movie:movie-detail", the_slug=slug)  # movie:movie-detail

    else:
        # update_date = timezone.now()
        order = Cart.objects.create(user_id=request.user)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect("movie:movie-detail", the_slug=slug)


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Movie, slug=slug)
    order_qs = Cart.objects.filter(
        user_id=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderMovie.objects.filter(
                item=item,
                user_id=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed to your cart")
            return redirect("cart:cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("movie:movie-detail", the_slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("movie:movie-detail", the_slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Movie, slug=slug)
    order_qs = Cart.objects.filter(
        user_id=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderMovie.objects.filter(
                item=item,
                user_id=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("cart:cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("movie:movie-detail", the_slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("movie:movie-detail", the_slug=slug)


@login_required
def add_simple_item_to_cart(request, slug):
    item = get_object_or_404(Movie, slug=slug)
    order_item, created = OrderMovie.objects.get_or_create(
        item=item,
        user_id=request.user,
        ordered=False
    )
    order_qs = Cart.objects.filter(user_id=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was update")
            return redirect("cart:cart")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect("cart:cart")
    else:
        # update_date = timezone.now()
        order = Cart.objects.create(user_id=request.user)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect("cart:cart")
