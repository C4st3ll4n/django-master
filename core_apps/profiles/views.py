from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from authors_api.settings.local import DEFAULT_FROM_EMAIL
from .exceptions import CantFollowYourself, NotYourProfile
from .models import Profile
from .pagination import ProfilePagination
from .rederers import ProfileJSONRenderer, ProfilesJSONRenderer
from .serializers import ProfileSerializer, FollowingSerializer, UpdateProfileSerializer

User = get_user_model()

"""
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_all_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    namespaced_response = {"profiles": serializer.data}

    return Response(namespaced_response, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_profile_details(request, username):
    try:
        user_profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        raise NotFound("A profile with this username does not exists")

    serializer = ProfileSerializer(user_profile, many=False)
    formatted_response = {"profile": serializer.data}
    return Response(formatted_response, status=status.HTTP_200_OK)
"""


class ProfileListAPIVIew(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    renderer_classes = (ProfilesJSONRenderer,)
    pagination_class = ProfilePagination


class ProfileDetailAPIVIew(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.select_related("user")
    renderer_classes = (ProfileJSONRenderer,)

    def retrieve(self, request, username, *args, **kwargs):
        try:
            profile = self.queryset.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound("A profile with this username does not exists")

        serializer = self.serializer_class(profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfileAPIVIew(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateProfileSerializer
    queryset = Profile.objects.select_related("user")
    renderer_classes = (ProfileJSONRenderer,)

    def patch(self, request, username):
        try:
            self.queryset.get(user__username=username)
        except Profile.DoesNotExist:
            raise NotFound("A profile with this username does not exists")

        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile

        data = request.data
        serializer = self.serializer_class(instance=request.user, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def get_my_followers(request, username):
    try:
        specific_user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise NotFound("A user with this username does not exists")

    user_profile_instance = Profile.objects.get(user__pkid=specific_user.pkid)
    user_followers = user_profile_instance.followed_by.all()
    serializer = FollowingSerializer(user_followers, many=True)

    formatted_response = {"status_code": status.HTTP_200_OK, "followers": serializer.data,
                          "num_of_followers": len(serializer.data)}

    return Response(formatted_response, status=status.HTTP_200_OK)


class FollowUnfollowAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowingSerializer

    def get(self, request, username):
        try:
            specific_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound("A user with this username does not exists")

        user_profile_instance = Profile.objects.get(user__pkid=specific_user.pkid)
        my_following_list = user_profile_instance.following_list()
        serializer = ProfileSerializer(my_following_list, many=True)
        formatted_response = {"status_code": status.HTTP_200_OK,
                              "users_i_follow": serializer.data,
                              "num_users_i_follow": len(serializer.data)}
        return Response(formatted_response, status=status.HTTP_200_OK)

    def post(self, request, username):
        try:
            specific_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound("A user with this username does not exists")

        if specific_user.pkid == request.user.pkid:
            raise CantFollowYourself

        user_profile_instance = Profile.objects.get(user__pkid=specific_user.pkid)
        current_user_profile = request.user.profile

        if current_user_profile.check_following(user_profile_instance):
            status_code = status.HTTP_400_BAD_REQUEST
            formatted_response = {
                "status_code": status_code,
                "errors": f"You already follow {specific_user.username}"
            }
            return Response(formatted_response, status=status_code)

        current_user_profile.follow(user_profile_instance)

        subject = "A new user follows you"
        message = f"Hi there {specific_user.username}, the user {current_user_profile.user.username} now follows you"

        from_email = DEFAULT_FROM_EMAIL
        recipient_list = [specific_user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        return Response(status=status.HTTP_200_OK, data={
            "status_code": status.HTTP_200_OK,
            "detail": f"You now follow {specific_user.username}"
        })

    def delete(self, request, username):
        try:
            specific_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound("A user with this username does not exists")

        user_profile_instance = Profile.objects.get(user__pkid=specific_user.pkid)
        current_user_profile = request.user.profile

        if not current_user_profile.check_following(user_profile_instance):
            status_code = status.HTTP_400_BAD_REQUEST
            formatted_response = {
                "status_code": status_code,
                "errors": f"You do not follow {specific_user.username}"
            }
            return Response(formatted_response, status=status_code)

        current_user_profile.unfollow(user_profile_instance)
        
        return Response(status=status.HTTP_200_OK, data={
            "status_code": status.HTTP_200_OK,
            "detail": f"You do not follow {specific_user.username} anymore"
        })
