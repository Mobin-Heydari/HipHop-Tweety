from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Albom, MusicAlbom



class AlbomesList(View):
    
    def get(self, request):
        albomes = Albom.objects.all()
        most_rated_albomes = albomes.order_by('-likes')[:6]
        
        return render(
            request, 'alboms/list.html', {
                'albomes' : albomes,
                'most_rated_albomes' : most_rated_albomes
            }
        )
        
        
class AlbomDetail(View):
    
    def get(self, request, slug):
        albome = get_object_or_404(Albom, slug=slug)
        albome_musices = MusicAlbom.objects.filter(albome=albome)
        
        return render(
            request, 'alboms/detail.html', {
                'albome' : albome,
            }
        )
        
        