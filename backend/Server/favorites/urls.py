from django.urls import path
from . import views


app_name = "favorite"


urlpatterns = [
    path('', views.UserFavoritesView.as_view(), name="favorites"),
]
