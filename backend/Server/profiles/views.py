from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import UserProfile





class ProfileView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            profile = get_object_or_404(
                UserProfile,
                user=request.user
            )
            
            return render(
                request, 'profiles/profile.html', {
                    'profile' : profile
                }
            )
        else:
            return redirect('/')
        
    def post(self, request):
        
        if request.user.is_authenticated == True:
            
            profile = get_object_or_404(
                UserProfile,
                user=request.user
            )
            
            profile.imgae = request.POST.get('image')
            profile.f_name = request.POST.get('fname')
            profile.l_name = request.POST.get('l_name')
            profile.commen_name = request.POST.get('commen_name')
            profile.bio = request.POST.get('bio')
            
            profile.save()
            return redirect(reverse('profile:profile_view'))
        else:
            return redirect('/')