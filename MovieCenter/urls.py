from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from apps.account.views import SiteLoginView, SiteSignupView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("movie/", include("apps.movie.urls")),
    path("cart/", include("apps.cart.urls")),
    path("checkout/", include("apps.checkout.urls")),
    path("account/", include("django.contrib.auth.urls")),
    path("account/", include("apps.account.urls")),
    path("login/", SiteLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SiteSignupView.as_view(), name="signup"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
