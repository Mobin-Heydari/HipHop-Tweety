from django.urls import path
from . import views


app_name = "favorite"


urlpatterns = [
    # Favorites page url
    path('', views.UserFavoritesView.as_view(), name="favorites"),
    # Music favorite (add&remove) url
    path('music-favorite/<slug:slug>/', views.UserMusicFavoriteView.as_view(), name="user_music_faver"),
    # Albume favorite (add&remove) url
    path('albume-favorite/<slug:slug>/', views.UserAlbumeFavoriteView.as_view(), name="user_albume_faver"),
]
