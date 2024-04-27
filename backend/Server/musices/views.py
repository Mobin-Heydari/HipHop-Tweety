from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Music, Genre, Comment
from .forms import CommentForm



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
        

class MusicesView(View):
    
    def get(self, request):
        
        musices = Music.objects.all()
        
        return render(request, 'musices/musices_list.html', {'musices':musices})
    

class MusicDetail(View):
    
    def get(self, request, slug):
        
        music = get_object_or_404(Music, slug=slug)
        
        return render(request, 'musices/music_detail.html', {'music':music})
    
    
    def post(self, request, slug, pk):
        
        form = CommentForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            
            music = get_object_or_404(
                Music,
                available=True,
                slug=slug
            )
            
            Comment.objects.create(
                music = music,
                comment = cd['comment'],
                title = cd['title']
            )
            
            return redirect('musices:music_detail', slug)
        
        return render(request, 'musices/detail.html', {'form' : form})