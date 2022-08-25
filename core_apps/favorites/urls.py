from django.urls import path, include
from .views import ListUserFavoriteArticlesAPIView, FavoriteAPIVIew

urlpatterns = [
    path("articles/me/", ListUserFavoriteArticlesAPIView.as_view(), name="my-favorites"),
    path("<slug:slug>/", FavoriteAPIVIew.as_view(), name="favorite-article"),
]
