from django.urls import path
from django.conf.urls import url
from .views import (
    CartDetailView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    add_simple_item_to_cart
)

app_name = "cart"

urlpatterns = [
    path("yourcart/", CartDetailView.as_view(), name="cart"),
    path("add-to-cart/<slug>/", add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<slug>/", remove_from_cart, name="remove_from_cart"),
    path("remove-single-item-from-cart/<slug>/", remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path("add-simple-item-to-cart/<slug>/", add_simple_item_to_cart, name="add-simple-item-to-cart"),
]
