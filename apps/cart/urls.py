from django.urls import path
from django.conf.urls import url
from .views import CartDetailView

app_name = "cart"

urlpatterns = [path("test/", CartDetailView.as_view(), name="cart")]
