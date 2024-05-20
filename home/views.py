from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from musices.models import Music
from alboms.models import Albom
from subscription.models import UserSubscription



class Home(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    most_popular_musices = Music.objects.all().order_by('-likes')[:7]
                    most_resent_musices = Music.objects.all().order_by('-release_date')[:7]
                    most_played_musices = Music.objects.all().order_by('-plays')[:7]
                    
                    most_popular_albums = Albom.objects.all().order_by('-likes')[:7]
                    
                    return render(
                        request, 'home/home.html', {
                            'most_popular_musices' : most_popular_musices,
                            'most_resent_musices' : most_resent_musices,
                            'most_played_musices' : most_played_musices,
                            
                            'most_popular_albums' : most_popular_albums
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')