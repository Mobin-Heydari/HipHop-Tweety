from django.shortcuts import render
from django.views import View
from subscription.models import SubscriptionPlan




class LandingPageView(View):
    
    def get(self, request):
        
        plans = SubscriptionPlan.objects.filter(is_active=True)
        
        return render(
            request, 'landing/index.html', {
                'plans' : plans
            }
        )