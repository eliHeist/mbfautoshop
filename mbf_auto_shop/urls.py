from django.contrib import admin
from django.urls import path, include

from .appsConfig import getAppUrls

import django_unicorn

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("unicorn/", include("django_unicorn.urls")),
    # path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += getAppUrls()