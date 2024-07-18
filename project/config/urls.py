from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("main.urls")),
    path("accounts/", include("accounts.urls")),
    path("carts/", include("carts.urls")),
]

if settings.DEBUG:
    urlpatterns+= [
        path('__debug__/', include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
