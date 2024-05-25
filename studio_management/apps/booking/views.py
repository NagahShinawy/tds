from rest_framework import viewsets, permissions
from .models import Studio
from .serializers import StudioSerializer
from .permissions import IsOwnerOrReadOnly, IsStudioOwner
from studio_management.apps.profiles.choices import ProfileType


class StudioViewSet(viewsets.ModelViewSet):
    serializer_class = StudioSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['retrieve', 'update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [IsStudioOwner]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Filter the queryset based on the user's profile.
        """
        user_profile = self.request.user.profile
        if user_profile.user_type == ProfileType.STUDIO_OWNER:
            return Studio.objects.filter(owner=user_profile)
        return Studio.objects.all()

