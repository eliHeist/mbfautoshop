from django.contrib import admin
from django.urls import path, include

from misc.api.api import api_router

from .appsConfig import getAppUrls

import django_unicorn

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("unicorn/", include("django_unicorn.urls")),
    
    path('api/', api_router.urls),
    # path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += getAppUrls()