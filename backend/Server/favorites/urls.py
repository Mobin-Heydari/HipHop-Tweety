from django.urls import path
from . import views


app_name = "favorite"


urlpatterns = [
    path('', views.Favorites.as_view(), name="favorites"),
    
    # Add urls
    path("add-music-favorite/<slug:slug>/", views.AddMusicFavorite.as_view(), name="add_music_favorite"),
    path("add-albume-favorite/<slug:slug>/", views.AddAlbomeFavorite.as_view(), name="add_albume_favorite"),
    
    # Remove urls
    path("remove-music-favorite/<slug:slug>/", views.RemoveMusicFavorite.as_view(), name="remove_music_favorite"),
    path("remove-albume-favorite/<slug:slug>/", views.RemoveAlbomeFavorite.as_view(), name="remove_albume_favorite"),
]
