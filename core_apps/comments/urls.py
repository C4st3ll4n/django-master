from django.urls import path

from .views import CommentAPIView, CommentUpdateDeleteAPIVIew

urlpatterns = [
    path("<slug:slug>/comment/", CommentAPIView.as_view(), name="comments"),
    path("slug:slug>/comment/<str:id>", CommentUpdateDeleteAPIVIew.as_view(), name="comment"),
]
