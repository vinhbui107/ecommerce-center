from django import forms
from apps.checkout.models import Order
import re


class CheckoutForm(forms.ModelForm):
    order_description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Order
        fields = ("fullname", "shipping_address", "phone_number", "order_description")

    def clean_fullname(self):
        fullname = self.cleaned_data['fullname']
        if not re.search(r'^\w+$', fullname):
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")
        return fullname

    def clean_shipping_address(self):
        shipping_address = self.cleaned_data['shipping_address']
        if not re.search(r'^\w+$', shipping_address):
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")
        return shipping_address

    def clean_order_description(self):
        order_description = self.cleaned_data['order_description']
        if not re.search(r'^\w+$', order_description):
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")
        return order_description
