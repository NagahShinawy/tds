from rest_framework import viewsets, permissions
from studio_management.apps.profiles.choices import ProfileType


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user.profile


class IsStudioOwner(permissions.BasePermission):
    """
    Custom permission to only allow studio owners to add new studios.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_staff:
            return True

        return request.user.profile.user_type == ProfileType.STUDIO_OWNER


class IsAdminOrStudioOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_staff or request.user.profile.user_type == ProfileType.STUDIO_OWNER)
