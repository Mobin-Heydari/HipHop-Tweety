from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import UserProfile
from subscription.models import UserSubscription




class ProfileView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    profile = get_object_or_404(
                        UserProfile,
                        user=request.user
                    )
                    
                    return render(
                        request, 'profiles/profile.html', {
                            'profile' : profile,
                            'subscription' : user_sub
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        
        
        
    def post(self, request):
        
        if request.user.is_authenticated == True:
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    profile = get_object_or_404(
                        UserProfile,
                        user=request.user
                    )
                    
                    if request.FILES.get('image'):
                        profile.image = request.FILES.get('image')
                        profile.save()
                        
                    if request.POST.get('f_name'):
                        profile.f_name = request.POST.get('f_name')
                        profile.save()
                        
                    if request.POST.get('l_name'):
                        profile.l_name = request.POST.get('l_name')
                        profile.save()
                        
                    if request.POST.get('commen_name'):
                        profile.commen_name = request.POST.get('commen_name')
                        profile.save()
                    
                    if  request.POST.get('bio'):
                        profile.bio = request.POST.get('bio')
                        profile.save()
                    
                    
                    return redirect(reverse('profile:profile_view'))
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
            
