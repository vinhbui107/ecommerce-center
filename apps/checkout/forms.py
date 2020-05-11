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

        string_is_valid = check_symbol(fullname)

        if string_is_valid:
            return fullname
        else:
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")

    def clean_shipping_address(self):
        shipping_address = self.cleaned_data['shipping_address']

        string_is_valid = check_symbol(shipping_address)

        if string_is_valid:
            return shipping_address
        else:
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")

    def clean_order_description(self):
        order_description = self.cleaned_data['order_description']
        string_is_valid = check_symbol(order_description)

        if string_is_valid:
            return order_description
        else:
            raise forms.ValidationError("Letters and numbers only. Please try again without symbols.")


def check_symbol(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(regex.search(string) == None):
        return True
    else:
        return False
