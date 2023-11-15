from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from .views import report

app_name = "front_end"
urlpatterns = [
    path("", report, name="report"),
]
