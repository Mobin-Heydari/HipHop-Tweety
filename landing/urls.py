from django.urls import path
from . import views




app_name = "landing"


urlpatterns = [
    path('', views.LandingPageView.as_view(), name="landing"),
    path('contact/', views.ContactView.as_view(), name="contact")
]
