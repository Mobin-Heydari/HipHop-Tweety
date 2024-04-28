from django.urls import path
from . import views


app_name = "musices"


urlpatterns = [
    # Musices urls
    path('list/', views.MusicesView.as_view(), name="musices_list"),
    path('detail/<slug:slug>', views.MusicDetail.as_view(), name="music_detail"),
]
