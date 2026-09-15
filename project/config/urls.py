from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("main.urls")),
    path("accounts/", include("accounts.urls")),
    path("carts/", include("carts.urls")),
    path("orders/", include("orders.urls")),
]