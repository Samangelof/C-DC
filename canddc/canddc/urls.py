from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .conf import ADMIN_SITE_URL


urlpatterns = [
    
    path(ADMIN_SITE_URL, admin.site.urls),
    path('api/v1/', include('auths.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
