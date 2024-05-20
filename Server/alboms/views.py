from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from .models import Albom, MusicAlbom, Comment, CommentReply
from . import forms
from subscription.models import UserSubscription


class AlbomesList(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    queryset = Albom.objects.all()
                    
                    most_rated_albomes = queryset.order_by('-likes')[:6]
                    
                    page_number = request.GET.get('page')
                    paginator = Paginator(queryset, 12)
                    queryset = paginator.get_page(page_number)
                    
                    return render(
                        request, 'alboms/list.html', {
                            'albomes' : queryset,
                            'most_rated_albomes' : most_rated_albomes
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        
        
class AlbomDetail(View):
    
    def get(self, request, slug):
        
        if request.user.is_authenticated == True:
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
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
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        
        
class AddCommentView(View):
    def post(self, request, slug, pk):
        
        if request.user.is_authenticated == True:
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
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
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        
        
        
class AddReplyView(View):
    
    def post(self, request, slug, pk):
        
        if request.user.is_authenticated == True:
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:

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
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        