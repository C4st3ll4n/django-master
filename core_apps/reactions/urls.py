from django.urls import path

from .views import APIView

urlpatterns = [
    path("<slug:slug>/", APIView.as_view(), name="user-reaction"),
]
