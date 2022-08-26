from django.urls import path

from .views import (
    ArticleCreateAPIView,
    ArticleDeleteAPIView,
    ArticleDetailAPIView,
    ArticleListAPIVIew,
)

urlpatterns = [
    path("all/", ArticleListAPIVIew.as_view(), name="all-articles"),
    path("create/", ArticleCreateAPIView.as_view(), name="create-article"),
    path("details/<slug:slug>/", ArticleDetailAPIView.as_view(), name="article-details"),
    path("delete/<slug:slug>/", ArticleDeleteAPIView.as_view(), name="delete-article")
]
