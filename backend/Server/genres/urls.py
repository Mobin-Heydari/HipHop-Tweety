from django.urls import path
from . import views


app_name = "genres"


urlpatterns = [
    # Genre Url
    path('', views.GenresView.as_view(), name="genres"),
    path('detail/<slug:slug>', views.GenreDetail.as_view(), name="genre_detail"),
]