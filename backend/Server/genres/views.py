from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Genre
from musices.models import Music


class GenresView(View):
    
    def get(self, request):
        
        genres = Genre.objects.all()
        
        return render(
            request, 'genres/list.html', {
                'genres' : genres
            }
        )



class GenreDetail(View):
    
    def get(self, request, slug):
        
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