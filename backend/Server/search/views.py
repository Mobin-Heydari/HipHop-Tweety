from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import Http404
from musices.models import Music
from alboms.models import Albom



class SearchView(View):
    
    def get(self, request):
        
        searched_data = request.GET.get('q')
        
        if searched_data is not None:
        
            searched_musices = Music.objects.filter(title__icontains=searched_data)
            
            searched_albumes = Albom.objects.filter(title__icontains=searched_data)
            
            if searched_albumes and searched_musices is not None:
                
                return render(
                    request, 'search/search.html', {
                        'searched_musices': searched_musices,
                        'searched_albumes' : searched_albumes,
                        'searched_data' : searched_data
                    }
                )
            else:
                raise Http404()
        else:
            raise Http404()