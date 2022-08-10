from django.urls import path

from .views import FollowUnfollowAPIView, ProfileDetailAPIVIew, UpdateProfileAPIVIew, ProfileListAPIVIew, \
    get_my_followers

urlpatterns = [
    path("all/", ProfileListAPIVIew.as_view(), name="all-profiles"),
    path("user/<str:username>", ProfileDetailAPIVIew.as_view(), name="details-profile"),
    path("update/<str:username>", UpdateProfileAPIVIew.as_view(), name="profile-update"),
    path("<str:username>/followers/", get_my_followers, name="my-followers"),
    path("<str:username>/follow/", FollowUnfollowAPIView.as_view(), name="follow-unfollow"),
]
