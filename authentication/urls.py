from django.urls import path
from . import views


app_name = "authentication"


urlpatterns = [
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('register/', views.Register.as_view(), name="register"),
    path('chek-otp/', views.CheckOtp.as_view(), name="check_otp"),
    
    # change password
    path('reset-password/', views.ResetPassword.as_view(), name="reset_password"),
    path('validate-reset-password-otp/', views.ValidatePasswordOtp.as_view(), name="validate_otp"),
    path('chnage-password/', views.ChangePassword.as_view(), name="change_password"),
]
