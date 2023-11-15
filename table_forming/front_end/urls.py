from django.urls import path

from .views import report

app_name = "front_end"
urlpatterns = [
    path("", report, name="report"),
]
