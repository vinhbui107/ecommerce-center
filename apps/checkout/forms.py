from django import forms
from apps.checkout.models import Order


class CheckoutForm(forms.Form):
    fullname = forms.CharField(label="Your Name", required=True)
    shipping_address = forms.CharField(label="Your Address", required=True)
    phone_number = forms.CharField(label="Your Phone Number", required=True)
    order_description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Order
