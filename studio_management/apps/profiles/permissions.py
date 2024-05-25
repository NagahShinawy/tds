from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    """
    Permission class that grants permission to administrators and profile owners.

    Attributes:
    - has_object_permission: Method that determines whether a user has permission to access a specific object.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to access the object.

        Args:
        - request: The HTTP request being made.
        - view: The view instance associated with the request.
        - obj: The object being accessed.

        Returns:
        - True if the user has permission, False otherwise.
        """
        if request.method == "GET":
            return True

        if request.user.is_staff:
            return True
        return obj.user == request.user
