from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from .models import UserFavorite, UserAlbomeFaver, UserMusicFaver

from musices.models import Music
from alboms.models import Albom



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


class AddMusicFavorite(View):
    
    def get(self, request, slug):
        
        if request.user.is_authenticated == True:
            
            user_favorite = get_object_or_404(
                UserFavorite, 
                user = request.user
            )
            
            music = get_object_or_404(
                Music, 
                slug = slug
            )
            
            faver = UserMusicFaver.objects.create(
                user_favorite = user_favorite,
                music = music
            )
            
            faver.save
            
            user_favorite.count += 1
            user_favorite.save()
            
            next_url = request.GET.get('next')
            
            if next_url is not None:
                return redirect(next_url)
            
            return redirect('albomees:musices_list')
        else:
            return redirect(reverse('users:login'))
        
class AddAlbomeFavorite(View):
    
    def get(self, request, slug):
        
        if request.user.is_authenticated == True:
            
            user_favorite = get_object_or_404(
                UserFavorite, 
                user = request.user
            )
            
            albome = get_object_or_404(
                Albom, 
                slug = slug
            )
            
            faver = UserAlbomeFaver.objects.create(
                user_favorite = user_favorite,
                albome = albome
            )
            
            faver.save
            
            user_favorite.count += 1
            user_favorite.save()
            
            next_url = request.GET.get('next')
            
            if next_url is not None:
                return redirect(next_url)
            
            return redirect('albomes:albomes_list')
        else:
            return redirect(reverse('users:login'))