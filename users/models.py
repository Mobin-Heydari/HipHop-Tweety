from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from . import managers



class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        verbose_name="ایمیل",
        unique=True
    )
    
    username = models.CharField(
        verbose_name="نام کاربر", 
        max_length=40,
        unique=True
    )
    
    joined = models.DateField(auto_now_add=True,)

    is_active = models.BooleanField(
        verbose_name="فعال",
        default=True
    )
    
    is_admin = models.BooleanField(
        verbose_name="ادمین", default=False
    )
    
    # Managers
    objects = managers.UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    
    class Meta:
        ordering = ['joined']
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"


    def __str__(self):
        return self.username
    

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin