from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.http import Http404
from musices.models import Music
from alboms.models import Albom
from subscription.models import UserSubscription


class SearchView(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    searched_data = request.GET.get('q')
        
                    if searched_data is not None:
        
                        searched_musices = Music.objects.filter(title__icontains=searched_data)
                        
                        searched_albumes = Albom.objects.filter(title__icontains=searched_data)
                        
                        if searched_albumes and searched_musices is not None:
                            
                            page_number = request.GET.get('page')
                            paginator = Paginator(searched_musices, 8)
                            queryset = paginator.get_page(page_number)
                            
                            return render(
                                request, 'search/search.html', {
                                    'searched_musices': queryset,
                                    'searched_albumes' : searched_albumes,
                                    'searched_data' : searched_data
                                }
                            )    
                        else:
                            raise Http404()
                    else:
                        raise Http404()
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        