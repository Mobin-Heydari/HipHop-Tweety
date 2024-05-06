from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('musices/', include('musices.urls', namespace="musices")),
    path('genres/', include('genres.urls', namespace="genres")),
    path('albomes/', include('alboms.urls', namespace="albomes")),
    path('auth/', include('authentication.urls', namespace="authentication")),
    path('profile/', include('profiles.urls', namespace="profile")),
    path('favorites/', include('favorites.urls', namespace="favorites")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
