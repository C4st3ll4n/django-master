from django.urls import path, include
from .views import APIView

urlpatterns = [
    path("<slug:slug>/", APIView.as_view(), name="user-reaction"),
]
