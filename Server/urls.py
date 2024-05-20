from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('musices.urls', namespace="musices")),
    path('genre/', include('genres.urls', namespace="genres")),
    path('albume/', include('alboms.urls', namespace="albomes")),
    path('auth/', include('authentication.urls', namespace="authentication")),
    path('profile/', include('profiles.urls', namespace="profile")),
    path('favorites/', include('favorites.urls', namespace="favorites")),
    path('subscription/', include('subscription.urls', namespace="subscription")),
    path('home/', include('home.urls', namespace="home")),
    path('', include('landing.urls', namespace="landing")),
    path('search/', include('search.urls', namespace="search")),
    path('payment/', include('payment.urls', namespace="payment")),
    path('events/', include('events.urls', namespace="events")),
    
    # PWA url
    path('', include('pwa.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
