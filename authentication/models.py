from django.db import models
from django.core import validators




class Otp(models.Model):
    
    email = models.EmailField(
        max_length=255,
        verbose_name="ایمیل",
        validators=[
            validators.EmailValidator
        ]
    )
    
    username = models.CharField(
        max_length=255,
        verbose_name="نام کاربری"
    )
    
    password = models.CharField(
        max_length=255,
        verbose_name="رمز عبور"
    )
    
    otp_code = models.IntegerField(
        verbose_name="کد otp"
    )
    
    token = models.CharField(
        verbose_name="توکن",
        max_length=100,
        unique=True
    )

    
    class Meta:
        verbose_name = "کد اعتبارسنجی"
        verbose_name_plural = "کدهای اعتبارسنجی"
        
        
    def __str__(self):
        return f'{self.id}---{self.email}---{self.otp_code}'
    

class ResetPasswordOtp(models.Model):
    
    otp_code = models.IntegerField(
        verbose_name="کد otp"
    )
    
    token = models.CharField(
        verbose_name="توکن",
        max_length=100,
        unique=True
    )
    
    email = models.EmailField(
        max_length=255,
        verbose_name="ایمیل",
        validators=[
            validators.EmailValidator
        ]
    )
    
    class Meta:
        verbose_name = "کد اعتبار سنجی رمزعبور"
        verbose_name_plural = "کد های اعتبار سنجی رمزعبور"
        
    
    def __str__(self):
        return f'{self.token}----{self.otp_code}'