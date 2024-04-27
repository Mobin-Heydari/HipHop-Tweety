from django.urls import path
from . import views


app_name = "musices"


urlpatterns = [
    # Musices urls
    path('musices-list/', views.MusicesView.as_view(), name="musices_list"),
    path('music-detail/<slug:slug>', views.MusicDetail.as_view(), name="music_detail"),
    
    
    # Genre Url
    path('genres-list/', views.GenresView.as_view(), name="genres_list"),
    path('genre-detail/<slug:slug>', views.GenreDetail.as_view(), name="genre_detail"),
]
