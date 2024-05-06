from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from .models import UserFavorite, UserAlbomeFaver, UserMusicFaver



class Favorites(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            
            user_favorites = get_object_or_404(
                UserFavorite, 
                user = request.user
            )
            
            return render(
                request, 'favorites/favorites.html', {
                    'favers' : user_favorites
                }
            )
        else:
            return redirect(reverse('users:login'))
