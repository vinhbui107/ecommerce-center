from django.urls import path
from .views import CartDetailView, add_to_cart, remove_from_cart

app_name = "cart"

urlpatterns = [
    path("", CartDetailView.as_view(), name="cart"),
    path("add/<slug>/", add_to_cart, name="add-to-cart"),
    path("remove/<slug>/", remove_from_cart, name="remove-from-cart"),
]
