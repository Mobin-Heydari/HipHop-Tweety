from django.db import models
from users.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="کاربر",
        on_delete=models.CASCADE, 
        related_name="user_profile"
    )
    
    bio = models.TextField(
        max_length=500, 
        blank=True, null=True,
        verbose_name="بیوگرافی"
    )
    
    image = models.ImageField(
        upload_to='profiles/',
        blank=True, null=True,
        verbose_name="تصویر پروفایل", 
    )

    full_name = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name="نام کامل کاربر",
    )
    
    
    def __str__(self):
        return f"{self.user.username}.....{self.full_name}"


    class Meta:
        verbose_name = "پروفایل کاربر"
        verbose_name_plural = "پروفایل کاربران"