from django.urls import path

from .views import FavoriteAPIVIew, ListUserFavoriteArticlesAPIView

urlpatterns = [
    path("articles/me/", ListUserFavoriteArticlesAPIView.as_view(), name="my-favorites"),
    path("<slug:slug>/", FavoriteAPIVIew.as_view(), name="favorite-article"),
]
