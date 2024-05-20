from django.contrib import admin
from .models import Otp, ResetPasswordOtp



admin.site.register(Otp)

admin.site.register(ResetPasswordOtp)