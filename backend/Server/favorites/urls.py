from django.urls import path
from . import views


app_name = "favorite"


urlpatterns = [
    path('', views.Favorites.as_view(), name="favorites")
]
