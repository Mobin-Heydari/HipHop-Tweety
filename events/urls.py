from django.urls import path
from . import views


app_name = "events"

urlpatterns = [
    path('', views.EventsList.as_view(), name="events_list"),
    path('detail/<slug:slug>/', views.EventDetail.as_view(), name="event_detail")
]
