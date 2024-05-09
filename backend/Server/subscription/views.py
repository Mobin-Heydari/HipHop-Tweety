from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import View
from .models import UserSubscription
from users.models import User



class SubscriptionPlansView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            
            return render(request, 'subscription/subscription_plans.html')
        else:
            return redirect('authentication:login')
