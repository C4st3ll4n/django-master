from django.urls import path, include
from .views import CommentUpdateDeleteAPIVIew, CommentAPIView

urlpatterns = [
    path("<slug:slug>/comment/", CommentAPIView.as_view(), name="comments"),
    path("slug:slug>/comment/<str:id>", CommentUpdateDeleteAPIVIew.as_view(), name="comment"),
]
