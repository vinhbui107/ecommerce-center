from django.views.generic import TemplateView


class CartDetailView(TemplateView):
    template_name = "cart/cart.html"
