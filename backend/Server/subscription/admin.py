from django.contrib import admin
from . import models


admin.site.register(models.UserSubscription)

admin.site.register(models.SubscriptionPlan)