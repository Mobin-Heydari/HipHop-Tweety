from django.urls import path
from . import views


app_name = "payment"


urlpatterns = [
    path('<str:name>/', views.PaymentView.as_view(), name="time_selection"),
    path('zarinpal/send/<int:pk>/', views.ZarinpalSendRequest.as_view(), name='zarinpal_send_request'),
    path('zarinpal/verify/', views.ZarinpalVerify.as_view(), name="zarinpal_verify")
]
