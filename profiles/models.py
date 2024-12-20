from django.db import models


class UserProfile(models.Model):
    
    user = models.OneToOneField(
        'users.User',
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

    f_name = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name="نام",
    )
    
    l_name = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name="نام خانوادگی",
    )
    
    commen_name = models.CharField(
        max_length=250,
        blank=True, null=True,
        verbose_name="نام نمایشی"
    )
    
    class Meta:
        verbose_name = "پروفایل کاربر"
        verbose_name_plural = "پروفایل کاربران"
    
       
    def __str__(self):
        return f"{self.user.username}.....{self.commen_name}"

