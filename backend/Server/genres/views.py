from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Genre


class GenresView(View):
    
    def get(self, request):
        
        genres = Genre.objects.all()
        
        return render(
            request, 'genres/list.html', {
                'genres' : genres
            }
        )

        