from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.views import View
from django.utils import timezone

from subscription.models import UserSubscription, SubscriptionPlan
from  users.models import User

import requests
import json


#? sandbox merchant 
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
CallbackURL = 'http://127.0.0.1:8080/payment/zarinpal/verify/'



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
        


class ZarinpalSendRequest(View):
    
    def get(self, request, pk):
        
        instance = get_object_or_404(
            SubscriptionPlan,
            id = pk
        )
        
        monthes = request.GET.get('monthes')
        
        price = instance.price_pre_month * int(monthes)
        
        request.session['price'] = str(price)
        request.session['monthes'] = str(monthes)
        request.session['plan'] = str(instance.id)
        request.session['user_id'] = str(request.user.id)
        
        data = {
        "MerchantID": settings.MERCHANT,
        "Amount": price,
        "Description": description,
        "Email": request.user.email,
        "CallbackURL": CallbackURL,
        }
        
        data = json.dumps(data)
        
        # set content length by data
        
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        
        try:
            response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
                else:
                    return {'status': False, 'code': str(response['Status'])}
            return response
    
        except requests.exceptions.Timeout:
            return {'status': False, 'code': 'timeout'}
        except requests.exceptions.ConnectionError:
            return {'status': False, 'code': 'connection error'}
        return redirect('/')


class ZarinpalVerify(View):
    
    def get(self, request, authority):
        
        price = request.session['price']
        
        data = {
        "MerchantID": settings.MERCHANT,
        "Amount": oprice,
        "Authority": authority,
        }
        
        data = json.dumps(data)
        
        # set content length by data
        
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        
        response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                
                user_id = request.session['user_id']
                
                user = User.objects.get(id=int(user_id))
                
                try:
                    user_sub = UserSubscription.objects.get(user=user)
                    
                    monthes = request.session['monthes']
                    plan = request.session['plan']
                    
                    now = timezone.now()
                    end_date = now + timezone.timedelta(days=30*int(monthes))
                    plan = SubscriptionPlan.objects.get(name=str(plan))
                    
                    user_sub.plan = plan
                    user_sub.end_date = end_date
                    user_sub.start_date = now
                    
                    user_sub.save()
                    return redirect('home:home')
                except user_sub.DoesNotExist:
                    
                    monthes = request.session['monthes']
                    plan = request.session['plan']
                    
                    now = timezone.now()
                    end_date = now + timezone.timedelta(days=30*int(monthes))
                    plan = SubscriptionPlan.objects.get(name=str(plan))
                    
                    user_sub = UserSubscription.objects.create(
                        user = user,
                        start_date = now,
                        end_date = end_date,
                        plan = plan,
                        is_active = True,
                    )
                    
                    user_sub.save()
                    
                    return redirect('home:home')
                return render(request, 'payment/success.html', {'order':order, 'RefID':response['RefID']})
            else:
                return render(request, 'payment/failed.html', {'order':order})
        return response