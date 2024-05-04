from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import UserProfile





class ProfileView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            profile = get_object_or_404(
                UserProfile, user=request.user
            )
            
            return render(
                request, 'profiles/profile.html', {
                    'profile' : profile
                }
            )
        else:
            return redirect('/')