from django.urls import path
from . import views


app_name = "alboms"


urlpatterns = [
    path("list/", views.AlbomesList.as_view(), name="albomes_list"),
    path("detail/<slug:slug>", views.AlbomDetail.as_view(), name="albome_detail")
]
