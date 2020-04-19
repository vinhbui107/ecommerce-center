from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import SiteLoginView, SiteSignupView
from movie.views import HomePageView, AboutView, ContactView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("movie/", include("movie.urls")),
    path("cart/", include("cart.urls")),
    path("checkout/", include("checkout.urls")),

    path("account/", include("django.contrib.auth.urls")),
    path("account/", include("account.urls")),
    path("login/", SiteLoginView.as_view(), name="login"),
    path("signup/", SiteSignupView.as_view(), name="signup"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
