from django.urls import path
from . import views


app_name = "subscription"

urlpatterns = [
    path("test/", views.test_subscription, name="test")
]
