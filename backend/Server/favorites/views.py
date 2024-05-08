from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from .models import UserMusicFavorite, UserAlbumFavorite

from musices.models import Music
from alboms.models import Albom



class UserFavoritesView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            
            user_musices_faver = UserMusicFavorite.objects.filter(user=request.user).order_by('-created')
            
            user_albums_faver = UserAlbumFavorite.objects.filter(user=request.user).order_by('-created')
            
            return render(
                request, 'favorites/favorites.html', {
                    'user_musices_faver' : user_musices_faver,
                    'user_albums_faver' : user_albums_faver
                }
            )
        else:
            return redirect(reverse('authentication:login'))