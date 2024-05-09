from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import View
from .models import UserSubscription, SubscriptionPlan
from users.models import User



class SubscriptionPlansView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            
            plans = SubscriptionPlan.objects.all()
            
            return render(
                request, 'subscription/subscription_plans.html', {
                    'plans' : plans
                }
            )
        else:
            return redirect('authentication:login')
