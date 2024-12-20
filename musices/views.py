from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Music, Comment,CommentReply
from .forms import CommentForm, ReplyForm
from alboms.models import Albom
from subscription.models import UserSubscription



class MusicesView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    queryset = Music.objects.all()
                    
                    albomes_queryset = Albom.objects.all()
                    
                    albomes_queryset = albomes_queryset.order_by('-likes')[0:5]
                    
                    page_number = request.GET.get('page')
                    paginator = Paginator(queryset, 15)
                    queryset = paginator.get_page(page_number)
                        
                    return render(
                        request, 'musices/musices_list.html', {
                            'musices' : queryset,
                            'alboms' : albomes_queryset,
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        
    

class MusicDetail(View):
    
    def get(self, request, slug):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    music = get_object_or_404(Music, slug=slug)
                    
                    music.plays += 1
                    
                    music.save()
                    
                    related_musices = Music.objects.filter(genre=music.genre)
                    
                    related_musices = related_musices.order_by('-likes')[:8]
                    
                    form = CommentForm()
                    reply = ReplyForm()
                    
                    return render(
                        request, 'musices/music_detail.html',
                        {
                            'music' : music,
                            'related_musices' : related_musices,
                            'form' : form,
                            'reply' : reply
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        
    
    
    def post(self, request, slug):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                      
                    form = CommentForm(request.POST)
                    
                    if form.is_valid():
                        
                        cd = form.cleaned_data
                        
                        music = get_object_or_404(
                            Music,
                            slug=slug
                        )
                        
                        comment = Comment.objects.create(
                            music = music,
                            user=request.user,
                            text = cd['comment'],
                            score = request.POST.get('score')
                        )
                        
                        comment.save()
                        
                        return redirect('musices:music_detail', slug)
                    
                    return render(request, 'musices/detail.html', {'form' : form})
                
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
            

class MusicCommentReply(View):
    
    def post(self, request, slug, pk):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    
                    form = ReplyForm(request.POST)
                    
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
                        
                        return redirect('musices:music_detail', slug)
                    else:
                        return redirect('musices:music_detail', slug)
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
