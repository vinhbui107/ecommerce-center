from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('movie.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('captcha/', include('captcha.urls')),
]
