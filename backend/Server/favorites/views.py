from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from .models import UserMusicFavorite, UserAlbumFavorite

from musices.models import Music
from alboms.models import Albom
from subscription.models import UserSubscription


class UserFavoritesView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    user_musices_faver = UserMusicFavorite.objects.filter(user=request.user).order_by('-created')
                    
                    user_albums_faver = UserAlbumFavorite.objects.filter(user=request.user).order_by('-created')
                    
                    return render(
                        request, 'favorites/favorites.html', {
                            'user_musices_faver' : user_musices_faver,
                            'user_albums_faver' : user_albums_faver
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
            
        

class UserMusicFavoriteView(View):
    
    def get(self, request, slug):
        
        if request.user.is_authenticated == True:
            
            try:
                
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    music = get_object_or_404(
                        Music, 
                        slug = slug
                    )
                    
                    try:
                        
                        faver = UserMusicFavorite.objects.get(
                            user = request.user,
                            music = music
                        )
                        
                        faver.delete()
                        
                        music.likes -= 1
                        music.save()
                        
                        return redirect('favorites:favorites')
                    except:
                        
                        faver = UserMusicFavorite.objects.create(
                            user = request.user,
                            music = music
                        )
                        
                        faver.save
                        
                        music.likes += 1
                        music.save()
                        
                        return redirect('favorites:favorites')   
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
            
        

class UserAlbumeFavoriteView(View):
    
    def get(self, request, slug):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    albume = get_object_or_404(
                        Albom, 
                        slug = slug
                    )
            
                try:
                    
                    faver = UserAlbumFavorite.objects.get(
                        user = request.user,
                        albume = albume
                    )
                    
                    faver.delete()
                    
                    albume.likes -= 1
                    albume.save()
                    
                    return redirect('favorites:favorites')
                except:
                    
                    faver = UserAlbumFavorite.objects.create(
                        user = request.user,
                        albume = albume
                    )
                    
                    faver.save
                    
                    albume.likes += 1
                    albume.save()
                    
                    return redirect('favorites:favorites')
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')