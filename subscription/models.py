from django.db import models
# from users.models import User
from django.utils import timezone



class SubscriptionPlan(models.Model):
    
    name = models.CharField(
        verbose_name="عنوان پلن اشتراک",
        max_length=200,
    )
    
    price_pre_month = models.IntegerField(
        verbose_name="قیمت پلن اشتراک برای هر ماه"
    )
    
    is_active = models.BooleanField(
        verbose_name="وضعیت پلن اشتراک",
        default=True,
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created']
        verbose_name = "پلن اشتراک"
        verbose_name_plural = "پلن های اشتراک"
        
    
    def __str__(self):
        return f'{self.name} price for month : {self.price_pre_month}'



class UserSubscription(models.Model):
    
    user = models.ForeignKey(
        'users.User',
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
    
    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.SET_NULL,
        related_name="plans",
        verbose_name="پلن",
        null=True
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
        
    def validated_day(self):
        if self.end_date < timezone.now():
            return 0
        else:
            return (self.end_date - timezone.now()).days