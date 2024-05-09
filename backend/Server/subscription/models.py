from django.db import models
from users.models import User
from django.utils import timezone


class UserSubscription(models.Model):
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_sub",
        verbose_name="کاربر",
    )
    
    start_date = models.DateTimeField(
        verbose_name="تاریخ شروع اشتراک"
    )
    
    end_date = models.DateTimeField(
        verbose_name="تاریخ اتمام اشتراک"
    )
    
    is_active = models.BooleanField(
        verbose_name="وضعیت اشتراک",
        default=False
    )
    
    class Meta:
        verbose_name = "اشتراک کاربر"
        verbose_name_plural = "اشتراک کاربران"
        
    def __str__(self):
        return f"{self.user.username} - {self.start_date} - {self.end_date} - {self.is_active}"
    
    def validate_subscription(self):
        if self.end_date < timezone.now():
            self.is_active = False
            self.save()
            return False
        else:
            self.is_active = True
            self.save()
            return True