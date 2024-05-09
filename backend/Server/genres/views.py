from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Genre
from musices.models import Music
from subscription.models import UserSubscription

class GenresView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    genres = Genre.objects.all()
        
                    return render(
                        request, 'genres/list.html', {
                            'genres' : genres
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        
        



class GenreDetail(View):
    
    def get(self, request, slug):
        
        if request.user.is_authenticated == True:
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    genre = get_object_or_404(Genre, slug=slug)
                    
                    genere_musices = Music.objects.filter(genre=genre).order_by('-likes')
                    
                    genres = Genre.objects.all().order_by('?')
                    
                    return render(
                        request, 'genres/detail.html', {
                            'genre' : genre,
                            'genres' : genres,
                            'genere_musices' : genere_musices
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')