from django.urls import path
from django.conf.urls import url
from apps.checkout.views import CheckoutView, CheckoutDoneView, checkout

app_name = "checkout"

urlpatterns = [
    path("", CheckoutView, name="checkout"),
    path("payment/", checkout, name="payment"),
    path("done/", CheckoutDoneView.as_view(), name="checkout-done"),
]
