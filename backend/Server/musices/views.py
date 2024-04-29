from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Music, Comment
from .forms import CommentForm
from alboms.models import Albom



class MusicesView(View):
    
    def get(self, request):
        
        musices_queryset = Music.objects.all()
        
        albomes_queryset = Albom.objects.all()
        
        albomes_queryset = albomes_queryset.order_by('-likes')[0:5]
        
        return render(
            request, 'musices/musices_list.html',
            {
                'musices' : musices_queryset,
                'alboms' : albomes_queryset
               
            }
        )
    

class MusicDetail(View):
    
    def get(self, request, slug):
        
        music = get_object_or_404(Music, slug=slug)
        
        related_musices = Music.objects.filter(genre=music.genre)
        
        related_musices = related_musices.order_by('-likes')[:8]
        
        return render(
            request, 'musices/music_detail.html',
            {
                'music' : music,
                'related_musices' : related_musices
            }
        )
    
    
    def post(self, request, slug):
        
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