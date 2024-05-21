from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator
from subscription.models import UserSubscription
from .models import Event, EventDescription



class EventsList(View):
    
    def get(self, request):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    queryset = Event.objects.all()
                    
                    page_number = request.GET.get('page')
                    paginator = Paginator(queryset, 8)
                    queryset = paginator.get_page(page_number)
                    
                    return render(
                        request, 'events/events.html', {
                            'event': queryset,
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')
        

class EventDetail(View):
    
    def get(self, request, slug):
        
        if request.user.is_authenticated == True:
            
            try:
                user_sub = UserSubscription.objects.get(user=request.user)
                
                user_sub.validate_subscription()
                
                if user_sub.is_active == True:
                    
                    event = get_object_or_404(
                        Event, slug=slug
                    )
                    
                    return render(
                        request, 'events/event_detail.html', {
                            'event': event,
                        }
                    )
                else:
                    return redirect('subscription:plans')
            except:
                return redirect('subscription:plans')
        else:
            return redirect('authentication:login')