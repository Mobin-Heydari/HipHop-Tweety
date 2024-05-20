from django.db import models
from django.core.validators import EmailValidator



class Contact(models.Model):
    
    f_name = models.CharField(
        verbose_name="نام",
        max_length=250,
        blank=True,
        null=True
    )
    
    l_name = models.CharField(
        verbose_name="نام خانوادگی",
        max_length=250,
        blank=True,
        null=True
    )
    
    phone = models.CharField(
        verbose_name="شماره تماس",
        max_length=12,
        blank=True,
        null=True
    )
    
    email = models.EmailField(
        validators=[EmailValidator],
        verbose_name="ایمیل",
        blank=True,
        null=True
    )
    
    message = models.TextField(
        verbose_name="پیام",
        blank=True,
        null=True
    )
    
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "تماس"
        verbose_name_plural = "تماس ها"


    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
    def auto_delete_contacts(self):
        if self.created < timezone.now() - timedelta(days=2):
            self.delete()