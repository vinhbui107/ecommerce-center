from django.views.generic import View, TemplateView
from django.forms.models import inlineformset_factory
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from apps.checkout.forms import CheckoutForm
from apps.account.models import CustomerUser
from apps.cart.models import Cart
from apps.checkout.models import Order


class CheckoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            # kiem tra xem use hien tai co order nao hay khong
            order_of_user = Order.objects.get(
                user_id=self.request.user, is_complete=False
            )
            # Neu nhu nguoi dung da co
            # Cap nhat la gia tien cua order
            cart_of_user = Cart.objects.filter(
                user_id=self.request.user, is_active=True
            )[0]
            order_of_user.order_total = float(cart_of_user.get_total())
            order_of_user.save()

            form = CheckoutForm()

            context = {"form": form, "cart": cart_of_user}
            return render(self.request, "checkout/checkout.html", context)

        except ObjectDoesNotExist:
            # neu nguoi dung chua co se tao moi 1 order
            cart_of_user = Cart.objects.filter(
                user_id=self.request.user, is_active=True
            )
            if cart_of_user.exists():  # kiem tra nguoi dung co gio hang nao khong
                cart = cart_of_user[0]
                new_order = Order.objects.create(
                    user_id=self.request.user,
                    cart_id=cart,
                    order_total=int(cart.get_total()),
                )
                return redirect("checkout:checkout")
            else:  # nguoi dung khong co movie nao trong gio hang
                return redirect("/")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST)
        try:
            order = Order.objects.get(user_id=self.request.user, is_complete=False)
            cart_of_user = Cart.objects.filter(
                user_id=self.request.user, is_active=True
            )[0]
            if form.is_valid():
                if order.cart_id == cart_of_user:
                    fullname = form.cleaned_data.get("fullname")
                    shipping_address = form.cleaned_data.get("shipping_address")
                    phone_number = form.cleaned_data.get("phone_number")
                    order_description = form.cleaned_data.get("order_description")

                    # save form
                    order.fullname = fullname
                    order.shipping_address = shipping_address
                    order.phone_number = phone_number
                    order.order_description = order_description
                    order.is_complete = True
                    order.save()

                    # change status cart and cart_movie
                    cart_of_user.is_active = False
                    cart_of_user.save()

                    for cart_movie in cart_of_user.movies.all():
                        cart_movie.is_active = False
                        cart_movie.save()

                    # send email success payment
                    messages = render_to_string("checkout/checkout_email.html", {
                        'name': order.user_id.username,
                    })
                    email = EmailMessage(
                        "Thank you for purchasing movies",
                        messages,
                        settings.DEFAULT_FROM_EMAIL,
                        [self.request.user.email],
                    )
                    email.fail_silently = False
                    email.send()

                # payment success
                return redirect("checkout:checkout-done")

            # user input not invalid
            return redirect("/")

        # user dont have any order
        except ObjectDoesNotExist:
            return redirect("/")


class CheckoutDoneView(LoginRequiredMixin, TemplateView):
    template_name = "checkout/checkout_done.html"
