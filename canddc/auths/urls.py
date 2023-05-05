from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import RegisterView, TokenView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', TokenView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
