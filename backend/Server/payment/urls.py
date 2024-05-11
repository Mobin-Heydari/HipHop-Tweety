from django.urls import path
from . import views


app_name = "payment"


urlpatterns = [
    path('<str:name>/', views.PaymentView.as_view(), name="time_selection")
]
