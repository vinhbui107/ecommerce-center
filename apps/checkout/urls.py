from django.urls import path
from django.conf.urls import url
from apps.checkout.views import CheckoutView, CheckoutDoneView

app_name = "checkout"

urlpatterns = [
    path("", CheckoutView.as_view(), name="checkout"),
    path("done/", CheckoutDoneView.as_view(), name="checkout-done"),
]
