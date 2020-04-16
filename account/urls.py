from django.urls import path
from django.conf.urls import url
from .views import AccountViewExample
app_name = 'account'

urlpatterns = [
    path('', AccountViewExample.as_view(), name='example_view'),
]
