from django.urls import path
from . import views


app_name = "subscription"

urlpatterns = [
    path("plans/", views.SubscriptionPlansView.as_view(), name="plans")
]
