from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Albom, MusicAlbom, Comment, CommentReply
from . import forms



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
        
        related_albomes = Albom.objects.filter(genre=albome.genre)
        related_albomes = related_albomes.order_by('?')[:6]
        
        comment_form = forms.CommentForm()
        reply_form = forms.ReplyForm()
        
        return render(
            request, 'alboms/detail.html', {
                'albome' : albome,
                'reply' : reply_form,
                'form' : comment_form,
                'related_albomes' : related_albomes
            }
        )
        
        
class AddCommentView(View):
    def post(self, request, slug, pk):
        if request.user.is_authenticated == True:
            form = forms.CommentForm(request.POST)
            
            if form.is_valid():
                
                cd = form.cleaned_data
                
                albome = get_object_or_404(
                    Albom,
                    pk=pk
                )
                
                comment = Comment.objects.create(
                    user = request.user,
                    albome = albome,
                    text = cd['comment'],
                    score = request.POST.get('score')
                )
                
                comment.save()
                
                return redirect('albomes:albome_detail', slug)
            else:
                return redirect('albomes:albome_detail', slug)
        else:
            return redirect('albomes:albome_detail', slug)
        
class AddReplyView(View):
    def post(self, request, slug, pk):
        if request.user.is_authenticated == True:
            form = forms.ReplyForm(request.POST)
            
            if form.is_valid():
                
                cd = form.cleaned_data
                
                comment = get_object_or_404(
                    Comment,
                    pk=pk
                )
                
                reply = CommentReply.objects.create(
                    comment = comment,
                    user=request.user,
                    reply = cd['reply'],
                )
                
                reply.save()
                
                return redirect('albomes:albome_detail', slug)
            else:
                return redirect('albomes:albome_detail', slug)
        else:
            return redirect('albomes:albome_detail', slug)