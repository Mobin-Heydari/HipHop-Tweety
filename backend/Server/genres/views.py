from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Genre


class GenresView(View):
    
    def get(self, request):
        
        genres = Genre.objects.all()
        
        return render(request, 'musices/genres.html', {'geners':genres})


class GenreDetail(View):
    
    def get(self, request, slug):
        
        genre = get_object_or_404(
            Genre, slug=slug
        )
        
        return render(request, 'musices/genre-detail', {'genre':genre})
        