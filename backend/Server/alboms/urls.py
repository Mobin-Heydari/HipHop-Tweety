from django.urls import path
from . import views


app_name = "alboms"


urlpatterns = [
    path("list/", views.AlbomesList.as_view(), name="albomes_list"),
    path("<slug:slug>/", views.AlbomDetail.as_view(), name="albome_detail"),
    path('add-comment/<slug:slug>/<int:pk>/', views.AddCommentView.as_view(), name="add_comment"),
    path('reply-comment/<slug:slug>/<int:pk>/', views.AddReplyView.as_view(), name="add_reply"),
]
