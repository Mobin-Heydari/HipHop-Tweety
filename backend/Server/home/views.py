from django.shortcuts import render
from django.views import View
from musices.models import Music
from alboms.models import Albom



class Home(View):
    
    def get(self, request):
        
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