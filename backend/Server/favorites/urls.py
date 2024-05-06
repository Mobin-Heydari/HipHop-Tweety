from django.urls import path
from . import views


app_name = "favorite"


urlpatterns = [
    path('', views.Favorites.as_view(), name="favorites"),
    
    # Add urls
    path("add-music-favorite/<slug:slug>/", views.AddMusicFavorite.as_view(), name="add_music_favorite"),
    path("add-albume-favorite/<slug:slug>/", views.AddAlbomeFavorite.as_view(), name="add_albume_favorite"),
]
