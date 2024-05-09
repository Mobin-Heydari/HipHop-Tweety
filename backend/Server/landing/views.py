from django.shortcuts import render, redirect
from django.views import View
from subscription.models import SubscriptionPlan
from .models import Contact



class LandingPageView(View):
    
    def get(self, request):
        
        plans = SubscriptionPlan.objects.filter(is_active=True)
        
        return render(
            request, 'landing/index.html', {
                'plans' : plans
            }
        )
        
class ContactView(View):
    
    def post(self, request):
        # Requested data
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            f_name = f_name,
            l_name = l_name,
            phone = phone,
            email = email,
            message = message
        )
        
        return redirect('/')