from django.contrib import admin
from django.urls import include, path
from django import settings

if not settings.TESTING:
    urlpatterns = [
        path("polls/", include("polls.urls")),
        path("admin/", admin.site.urls),
        path("__debug__/", include("debug_toolbar.urls")),
    ]