from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnlu(BasePermission):
    message = "You are not allowed to update or delete an article that does not belong to you"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
