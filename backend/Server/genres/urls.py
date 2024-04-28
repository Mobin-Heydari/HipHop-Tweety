from django.urls import path
from . import views


app_name = "genres"


urlpatterns = [
    # Genre Url
    path('genres-list/', views.GenresView.as_view(), name="genres_list"),
    path('genre-detail/<slug:slug>', views.GenreDetail.as_view(), name="genre_detail"),
]