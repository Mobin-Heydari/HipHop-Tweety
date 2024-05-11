from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from subscription.models import UserSubscription, SubscriptionPlan





class PaymentView(View):
    def get(self, request, name):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == False:
                    
                    plan = get_object_or_404(SubscriptionPlan, name=name)
        
                    return render(
                        request, 'payment/payment.html',{
                            'plan': plan
                        }
                    )
                else:
                    return redirect('home:home')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')